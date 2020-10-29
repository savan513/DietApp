import random
import string
from email.mime.image import MIMEImage

from .app_settings import MY_SETTING
from django.contrib.auth.decorators import login_required
import base64
from django.db.models.functions import Coalesce
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.shortcuts import render, redirect, HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import json
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from sqlite3 import IntegrityError
from PayTm import Checksum
import calendar
from .models import *
from datetime import datetime, date
from datetime import timedelta
import uuid
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import get_template, render_to_string

from django.contrib.staticfiles import finders

MERCHANT_KEY = 'qMhXQfCgo3uY#XYX'
MERCHANT_ID="ldvzTL73084002477842"
import razorpay

client = razorpay.Client(auth=("rzp_test_WKDV18b2fVQhU3", "uJzL5MBJKYXKPF8zuEjxdbmZ"))


def index(request):
    plans = Plans.objects.all()
    dietitians = dietitian.objects.all()
    feeds = feedback.objects.all()
    posters = poster.objects.all().reverse()
    count = poster.objects.all().count()
    param = {'plans': plans, 'dietitians': dietitians, 'feeds': feeds, 'posters': posters, 'count': count}
    MyUser.objects.filter(is_active=False).delete()

    return render(request, "index.html", param)

@transaction.atomic
def save_and_pay(request):
    param={'msg':False}
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        plan_id=request.POST['plan_id']
        plan = Plans.objects.get(id=plan_id)
        code = request.POST.get('referral','')

        try:
            user=MyUser.objects.create_user(username=username,email=email,is_customer=True,password=password,is_active=False)
            user.save()

            userdata=UserData()
            userdata.payment_uuid=uuid.uuid1().hex
            userdata.user=user
            userdata.plan=plan
            userdata.save()
        except:
           pass
        try:
            if code:
                udata = UserData.objects.get(referral_code=code)
                if udata:
                    udata.points += 20
                    udata.save()
                    userdata.points += 20
                    userdata.save()
        except:
            pass


        try:
            param_dict = {

                'MID': MERCHANT_ID,
                'ORDER_ID': str(userdata.payment_uuid),
                'TXN_AMOUNT': str(plan.price),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

            return render(request, 'paytm.html', {'param_dict': param_dict})



        except IntegrityError:
            transaction.rollback()
            messages.error(request, "Some Thing Went Wrong")
    return redirect("Home")


@csrf_exempt
@transaction.atomic
def handlerequest(request):
    form = request.POST
    response_dict = {}
    checksum=''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:

        if response_dict['RESPCODE'] == '01':

            payment_uuid = response_dict['ORDERID']
            txn_id = response_dict['TXNID']
            amount=response_dict['TXNAMOUNT']

            userdata=UserData.objects.get(payment_uuid=payment_uuid)
            userdata.is_paid=True

            userdata.save()
            user = MyUser.objects.get(id=userdata.user.id)
            user.is_active=True
            user.save()
            request.session['customer_fill'] = user.id
            payment1 = payment(user_id=userdata, transaction_id=txn_id, plan_id=userdata.plan,
                               amount=userdata.plan.price, date=date.today(), time=datetime.now().strftime("%H:%M:%S"))
            payment1.save()



            msg=f"""        
                <html><body>
<div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">
 
    <div class="row" style="margin-left:15%">
        <div class="col-12">
            <h5 style="color:#6BCCBA;font-size:20px;">Your Payment is Successful Done on SastaDiet</h5>
        </div>
    </div>
    <div class="row" style="margin-left:15%">
        <div class="col-12">
            <h5 style="color:#6BCCBA">Transaction id : {txn_id}</h5>
        </div>
        <div class="col-12">
            <h5 style="color:#6BCCBA">Transaction Amount : {amount}</h5>
        </div></div> </div>
</body>
</html>
            """
            email = EmailMultiAlternatives(
                subject="Welcome to Sastadiet",
                body=msg,
                from_email=MY_SETTING,
                to=[user.email],

            )
            email.mixed_subtype = 'related'

            email.content_subtype = "html"
            email.send()

        else:
            payment_uuid = response_dict['ORDERID']
            udata=UserData.objects.get(payment_uuid=payment_uuid)
            if udata.points > 0:
                udata.points -=20
            udata.save()
            user=MyUser.objects.get(id=udata.user.id)
            user.delete()



    return render(request, 'paymentstatus.html', {'response': response_dict})

def sendrequest(request):
    if request.session.has_key('customer'):
        if request.method == "POST":
            type = request.POST['radiotype']
            time = request.POST['time']
            date = request.POST['date']
            time1 = datetime.strptime(time, '%H:%M')

            end_time = time1 + timedelta(minutes=15)

            if type == "call":
                udata = UserData.objects.get(user=request.user)

                udata.save()
            meeting1 = meeting(user=request.user.userdata, dietitian=request.user.userdata.dietitian, date=date,
                               time=time, end_time=end_time, status=0, created_at=datetime.today(),
                               updated_at=datetime.today(), type=type)
            meeting1.save()

            try:
                msg = f"""   <html><body>
                           <div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">


                               <div class="row" style="margin-left:15%">
                                   <div class="col-12">
                                       <h5 style="color:#6BCCBA">Your {type} Meeting Request is Successfully sent to your Dietitian {request.user.userdata.dietitian}</h5>
                                   </div>
                               </div>    
                           </body>
                           </html>
                                       """
                email = EmailMultiAlternatives(
                    subject="Meeting Request Status",
                    body=msg,
                    from_email=MY_SETTING,
                    to=[request.user.email],

                )
                email.mixed_subtype = 'related'

                email.content_subtype = "html"
                email.send()
            except:
                messages.error(request, "Your Email is Not SSent please try again")

        return redirect("userdashboard")
    else:
        return redirect("Home")


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        cont = Contact(name=name, email=email, subject=subject, message=message)
        cont.save()

        try:
            msg = f"""         <html><body>
                           <div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">

                               <div class="row" style="margin-left:15%">
                                   <div class="col-12">
                                       <h5 style="color:#6BCCBA;font-size:20px;">Dear SastaDiet Owner one Customer want to ask/tell something</h5>
                                   </div>
                               </div>
                               <div class="row" style="margin-left:15%">
                                   <div class="col-12">
                                       <h5 style="color:#6BCCBA">Name : {name}</h5>
                                   </div>
                                   <div class="col-12">
                                       <h5 style="color:#6BCCBA">Email : {email}</h5>
                                   </div>
                                   <div class="col-12">
                                       <h5 style="color:#6BCCBA">Subject : {subject}</h5>
                                   </div>

                                    <div class="col-12">
                                       <h5 style="color:#6BCCBA">Message : {message}</h5>
                                   </div>

                                   </div> </div>
                           </body>
                           </html>
                                       """
            email = EmailMultiAlternatives(
                subject="Customer's Query",
                body=msg,
                from_email=MY_SETTING,
                to=['harshpatel281199@gmail.com'],

            )
            email.mixed_subtype = 'related'

            email.content_subtype = "html"
            email.send()
        except:
            messages.error(request, "Your Email is Not Sent")

        messages.success(request, "Successfully Sent")

    return redirect("Home")


def getplan(request):
    if request.method == "GET":
        id = request.GET['id']

        plandetail = Plans.objects.get(id=id)

        response1 = json.dumps(
            {'plan_title': plandetail.title, 'plan_price': plandetail.price, 'plan_id': plandetail.id})
        return HttpResponse(response1)


@login_required(login_url="/")
def userdashboard(request):
    if request.session.has_key('customer'):

        id = request.session['customer']
        user = MyUser.objects.get(id=id)
        meetings = meeting.objects.filter(user=request.user.userdata).order_by(('-date'))

        plusplans = Plans.objects.filter(is_plusplan=True, is_healthissue=request.user.userdata.plan.is_healthissue)
        amt_pay = float(plusplans[0].price) - float(request.user.userdata.plan.price)

        is_room = False
        plans = Plans.objects.all()
        conf_met = False
        try:
            conf_met = meeting.objects.get(status=3, user=request.user.userdata)
            if conf_met:
                is_room = True
        except:
            pass

        report_message = None
        achive = None
        if request.session.has_key('report_msg'):
            report_message = request.session['report_msg']
            achive = request.session['achive']
            del request.session['report_msg']
        param = {'meetings': meetings, 'amt_pay': amt_pay, 'is_room': is_room, 'plusplans': plusplans, 'plans': plans,
                 'conf_met': conf_met, 'report_message': report_message, 'achive': achive}
        return render(request, "userdashboard.html", param)

    return redirect("Home")


def updateplan(request,id):
   if request.session.has_key('customer'):
       id = id

       plan = Plans.objects.get(id=id)
       paid_price = request.user.userdata.plan.price
       price_to_pay = 0
       if paid_price > plan.price:
           price_to_pay = paid_price - plan.price
       else:
           price_to_pay = plan.price - paid_price
       payment_uuid = uuid.uuid1().hex
       udata = UserData.objects.get(user=request.user)
       udata.payment_uuid=payment_uuid
       udata.updates_at=datetime.today()

       udata.save()
       param_dict=None
       try:
           param_dict = {

               'MID': MERCHANT_ID,
               'ORDER_ID': str(payment_uuid),
               'TXN_AMOUNT': str(price_to_pay),
               'CUST_ID': str(request.user.email),
               'INDUSTRY_TYPE_ID': 'Retail',
               'WEBSITE': 'SastaDiet',
               'CHANNEL_ID': 'WEB',
               'CALLBACK_URL': 'http://127.0.0.1:8000/handleplanchange/',

           }
           param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
       except IntegrityError:
           transaction.rollback()
           messages.error(request, "Some Thing Went Wrong")

       return render(request, 'paytm.html', {'param_dict': param_dict})


@csrf_exempt
@transaction.atomic
def handleplanchange(request):
    form = request.POST
    response_dict = {}
    checksum=''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:

        if response_dict['RESPCODE'] == '01':

            payment_uuid = response_dict['ORDERID']
            txn_id = response_dict['TXNID']
            amount=response_dict['TXNAMOUNT']

            userdata=UserData.objects.get(payment_uuid=payment_uuid)
            plan = Plans.objects.get(is_plusplan=True, is_healthissue=userdata.plan.is_healthissue)
            userdata.plan = plan
            userdata.save()

            payment1 = payment(user_id=userdata, transaction_id=txn_id, plan_id=userdata.plan,
                               amount=userdata.plan.price, date=date.today(), time=datetime.now().strftime("%H:%M:%S"))
            payment1.save()


            msg = f"""<html><body>
                        <div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">
                         
                            <div class="row" style="margin-left:15%">
                                <div class="col-12">
                                    <h5 style="color:#6BCCBA;font-size:20px;">Your Plan is Successfully Changed</h5>
                                </div>
                            </div>
                             <div class="row" style="margin-left:15%">
                                    <div class="col-12">
                                        <h5 style="color:#6BCCBA">Transaction id : {txn_id}</h5>
                                    </div>
                                    <div class="col-12">
                                        <h5 style="color:#6BCCBA">Transaction Amount : {amount}</h5>
                                    </div></div> 
                        </body>
                        </html>
                                    """
            email = EmailMultiAlternatives(
                subject="About Plan Change",
                body=msg,
                from_email=MY_SETTING,
                to=[userdata.user.email],

            )
            email.mixed_subtype = 'related'

            email.content_subtype = "html"
            email.send()
        else:
            payment_uuid = response_dict['ORDERID']
            udata=UserData.objects.get(payment_uuid=payment_uuid)
            plan=Plans.objects.get(is_plusplan=False,is_healthissue=udata.plan.is_healthissue)
            udata.plan=plan
            udata.save()
            user=MyUser.objects.get(id=udata.user.id)
            user.delete()




    return render(request, 'paymentstatus.html', {'response': response_dict,'is_planchange':True,'is_update':False})


def dietitiandashboard(request):
    if request.session.has_key('dietitian'):

        user_smart = UserData.objects.filter(plan__is_plusplan=False, dietitian=request.user.dietitian)
        user_plus = UserData.objects.filter(plan__is_plusplan=True, dietitian=request.user.dietitian)

        diet_pending_smart = UserData.objects.filter(is_chart_sent=False, dietitian=request.user.dietitian,
                                                     is_paid=True)
        diet_pending_smart_count = UserData.objects.filter(is_chart_sent=False,
                                                           dietitian=request.user.dietitian).count()

        pending_meeting_request = meeting.objects.filter(status=0, dietitian=request.user.dietitian)
        pending_meeting_request_count = meeting.objects.filter(status=0, dietitian=request.user.dietitian).count()
        accepted_request = meeting.objects.filter(status=1, dietitian=request.user.dietitian)
        user_count = UserData.objects.filter(dietitian=request.user.dietitian).count()
        weekly_report = Week_Report.objects.filter(user__dietitian=request.user.dietitian)

        param = {'user_smart': user_smart, 'user_plus': user_plus, 'diet_pending_smart': diet_pending_smart,
                 'pending_meeting_request': pending_meeting_request, 'accepted_request': accepted_request,
                 'user_count': user_count, 'pending_meeting_request_count': pending_meeting_request_count,
                 'weekly_report': weekly_report, 'diet_pending_smart_count': diet_pending_smart_count}

        return render(request, 'Dietitian.html', param)
    else:
        return redirect("Home")


def loginProcess(request):
    if request.method == "POST":

        user = authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', ''))

        if user is not None:
            if user.is_customer:
                if not user.userdata.is_data_filled:
                    request.session['customer_fill'] = user.id
                    resp = json.dumps({'msg': 'fillform', 'redirect': 'filluserdata'})

                    return HttpResponse(resp)

                request.session['customer'] = user.id
                login(request, user)
            if user.is_dietitian:
                request.session['dietitian'] = user.id
                login(request, user)

            if user.is_admin:
                request.session['admin'] = user.id
                login(request, user)
            resp = json.dumps({'msg': 'success'})
            return HttpResponse(resp)
        else:
            resp = json.dumps({'msg': 'Invalid Data'})
            return HttpResponse(resp)

    messages.info(request, 'Please Click on Signin')
    return redirect("Home")


@csrf_exempt
@transaction.atomic
def filluserdata(request):
    if request.method == "POST":

        id = int()
        if request.session.has_key('customer_fill'):
            id = request.session['customer_fill']
            user = MyUser.objects.get(id=id)
            fname = request.POST['firstname']
            mname = request.POST['middlename']
            lname = request.POST['lastname']
            age = request.POST['age']
            gender = request.POST['radiogender']
            mobile_no = request.POST['mobile_no']
            city = request.POST['address']
            height = request.POST['height']
            weight = request.POST['weight']
            userd = UserData.objects.get(user=user)
            userd.firstname = fname
            userd.lastname = lname
            userd.middlename = mname
            userd.age = age
            userd.gender = gender
            userd.city = city
            userd.mobile_no = mobile_no
            userd.height = height
            userd.weight = weight
            userd.updates_at = datetime.today()
            userd.date_tofill_form = datetime.today() + timedelta(days=7)
            days_in_month = calendar.monthrange(datetime.today().year, datetime.today().month)[1]

            userd.plan_end_date = datetime.today() + timedelta(days=days_in_month)
            userd.is_data_filled = True
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(8))
            user2 = None
            try:
                user2 = UserData.objects.get(referral_code=result_str)
            except:
                user2 = None
            if user2:
                while not user2:
                    letters = string.ascii_lowercase
                    result_str = ''.join(random.choice(letters) for i in range(8))
                    user2 = UserData.objects.get(referral_code=result_str)

            userd.referral_code = result_str

            userd.save()

            workout = request.POST['radio-workout']
            if workout == 'yes':
                workout = True
            else:
                workout = False
            workout_type = request.POST.getlist('workout_type', '')

            workout_time = request.POST.get('radio-workout-time', '')
            time_day = request.POST.get('time_day', '')
            day_week = request.POST.get('day_week', '')
            achive = request.POST['achive']
            food_type = request.POST['food_type']
            disease = request.POST['radio-disease']
            dishes = request.POST['radio-dishes']
            protien = request.POST['protien']
            about = request.POST['about']
            if disease == 'yes':
                disease = True
            else:
                disease = False
            uhealth = UserHealthData(userdata=userd, workout=workout, workout_time=workout_time,
                                     workout_time_inday=time_day, workout_day_inweek=day_week, want_to_achive=achive,
                                     type=food_type, dishes=dishes, have_disease=disease, supplements=protien,
                                     about=about)
            uhealth.save()

            for type in workout_type:
                wtype = Workout_type(type=type, user=uhealth)
                wtype.save()

            del request.session['customer_fill']

        else:

            return redirect("Home")
        messages.success(request, "Your Data is added please make login")
        return redirect("Home")
    else:

        return render(request, 'userdetail.html')


@csrf_exempt
@transaction.atomic
def checkfilleddata(request):
    if request.method == "POST":

        fname = request.POST['firstname']
        mname = request.POST['middlename']
        lname = request.POST['lastname']
        age = request.POST['age']
        gender = request.POST['radiogender']
        mobile_no = request.POST['mobile_no']
        city = request.POST['address']
        height = request.POST['height']
        weight = request.POST['weight']
        userd = UserData.objects.get(user=request.user)
        userd.firstname = fname
        userd.lastname = lname
        userd.middlename = mname
        userd.age = age
        userd.gender = gender
        userd.city = city
        userd.mobile_no = mobile_no
        userd.height = height
        userd.weight = weight
        userd.updates_at = datetime.today()
        userd.date_tofill_form = datetime.today() + timedelta(days=7)
        days_in_month = calendar.monthrange(datetime.today().year, datetime.today().month)[1]

        userd.plan_end_date = datetime.today() + timedelta(days=days_in_month)
        userd.is_data_filled = True
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        user2 = None
        try:
            user2 = UserData.objects.get(referral_code=result_str)
        except:
            user2 = None
        if user2:
            while not user2:
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(8))
                user2 = UserData.objects.get(referral_code=result_str)

        userd.referral_code = result_str

        userd.save()

        userd.save()

        workout = request.POST['radio-workout']
        if workout == 'yes':
            workout = True
        else:
            workout = False
        workout_type = request.POST.getlist('workout_type', request.user.userdata.userhealthdata.workout_type)

        workout_time = request.POST.get('radio-workout-time', '')
        time_day = request.POST.get('time_day', '')
        day_week = request.POST.get('day_week', '')
        achive = request.POST['achive']
        food_type = request.POST['food_type']
        disease = request.POST['radio-disease']
        dishes = request.POST['radio-dishes']
        protien = request.POST['protien']
        about = request.POST['about']
        if disease == 'yes':
            disease = True
        else:
            disease = False
        uhealth = UserHealthData(userdata=userd, workout=workout, workout_time=workout_time,
                                 workout_time_inday=time_day, workout_day_inweek=day_week, want_to_achive=achive,
                                 type=food_type, dishes=dishes, have_disease=disease, supplements=protien, about=about)
        uhealth.save()

        w_type = Workout_type.objects.filter(user=uhealth)
        w_type.delete()
        try:
            if workout_type:
                for type in workout_type:
                    wtype = Workout_type(type=type, user=uhealth)
                    wtype.save()
        except:
            pass
        return redirect("userdashboard")
    else:

        return redirect("filluserdata")


@transaction.atomic
def updatedata(request):
    if request.session.has_key('customer'):
        if request.method == "POST":
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            age = request.POST['age']
            gender = request.POST['radiogender']
            mobile_no = request.POST['mobile_no']
            uname = request.POST['uname']
            email = request.POST['email']

            height = request.POST['height']
            weight = request.POST['weight']
            user1 = MyUser.objects.get(id=request.user.id)
            udata = UserData.objects.get(user=request.user)
            user1.username = uname
            user1.email = email

            udata.firstname = fname
            udata.middlename = mname
            udata.lastname = lname
            udata.age = age
            udata.gender = gender
            udata.mobile_no = mobile_no
            udata.updates_at = datetime.today()
            udata.height = height
            udata.weight = weight
            user1.save()
            update_session_auth_hash(request, user1)
            try:
                udata.save()

                messages.success(request, "Successfully Changed")
            except:
                messages.success(request, "Something Went Wrong")
                transaction.rollback()
        return redirect("userdashboard")
    if request.session.has_key('dietitian'):
        if request.method == "POST":
            fname = request.POST['fname']
            mname = request.POST['mname']
            lname = request.POST['lname']
            uname = request.POST['uname']

            mobile_no = request.POST['mobile_no']
            qualification = request.POST['qualification']
            email = request.POST['email']
            image = ""
            if request.FILES.get('image') == None:
                image = request.user.dietitian.image
            else:
                image = request.FILES['image']

            user1 = MyUser.objects.get(id=request.user.id)
            dietitian1 = dietitian.objects.get(user=request.user)
            user1.username = uname
            user1.email = email

            dietitian1.firstname = fname
            dietitian1.middlename = mname
            dietitian1.lastname = lname
            dietitian1.qualification = qualification
            dietitian1.mobile_no = mobile_no
            dietitian1.image = image

            user1.save()
            update_session_auth_hash(request, user1)
            try:
                dietitian1.save()

                messages.success(request, "Successfully Changed")
            except:
                messages.success(request, "Something Went Wrong")
                transaction.rollback()
        return redirect("dietitiandashboard")
    return redirect("Home")


def logoutProcess(request):
    logout(request)
    if request.session.has_key('customer'):
        del request.session['customer']
    if request.session.has_key('dietitaion'):
        del request.session['dietitaion']
    if request.session.has_key('admin'):
        del request.session['admin']

    return redirect("Home")


def checkusername(request):
    uname = request.GET['uname']
    user = None
    try:
        user = MyUser.objects.get(username=uname)
    except:
        pass
    is_available = bool
    if user:
        is_available = True
    else:
        is_available = False
    response1 = json.dumps({'is_available': is_available})
    return HttpResponse(response1)


def checkemail(request):
    email = request.GET['email']
    user = None
    try:
        user = MyUser.objects.get(email=email)
    except:
        pass
    is_available = bool
    if user:
        is_available = True
    else:
        is_available = False

    response1 = json.dumps({'is_available': is_available})
    return HttpResponse(response1)


def acceptrequest(request, id):
    if request.session.has_key('dietitian'):
        met = meeting.objects.get(id=id)
        met.status = 1
        met.save()
        if met.type == 'call':
            met.user.call_count = met.user.call_count + 1
        met.user.save()
        return redirect('dietitiandashboard')
    return redirect("Home")


def deleterequest(request, id):
    if request.session.has_key('dietitian'):
        met = meeting.objects.get(id=id)
        met.status = 2
        met.save()
        return redirect('dietitiandashboard')
    return redirect("Home")


def senddietchart(request):
    if request.session.has_key('dietitian'):
        id = request.GET.get('id', '')
        udata = UserData.objects.get(user__id=id)
        email = udata.user.email
        try:
            com = 0
            udata.is_chart_sent = True

            if udata.plan.title == "SMART PLAN":

                com = request.user.dietitian.commission_smartplan
            elif udata.plan.title == "SMART + PLAN":

                com = request.user.dietitian.commission_smartplusplan
            elif udata.plan.title == "SMART PLAN FOR HEALTH ISSUES":

                com = request.user.dietitian.commission_smartplan_healthissue
            elif udata.plan.title == "SMART + PLAN FOR HEALTH ISSUES":

                com = request.user.dietitian.commission_smartplusplan_healthissue

            request.user.dietitian.revenue = request.user.dietitian.revenue + com
            udata.save()
            request.user.dietitian.save()

            resp = json.dumps({"msg": "chart sent", 'email': email})

            return HttpResponse(resp)


        except:

            resp = json.dumps({"msg": "error"})
            return HttpResponse(resp)

    return HttpResponse("Error 404")


@transaction.atomic
def review(request):
    if request.method == "POST":
        name = request.user.username
        rev = request.POST['review']

        feed = feedback(name=name, review=rev, datetime=datetime.today())
        try:
            feed.save()
            request.user.userdata.is_feed_remain = False
            request.user.userdata.save()
            messages.success(request, "Your Feedback Saved Successfully")

        except:
            transaction.rollback()
            messages.error(request, "Something Went Wrong")
        return redirect('userdashboard')

    return redirect("Home")


def checkrefferalcode(request):
    code = request.GET.get('code', '')
    try:
        udata = UserData.objects.get(referral_code=code)
        if udata:
            resp = json.dumps({'check': 'success'})
            return HttpResponse(resp)
        else:
            resp = json.dumps({'check': 'fail'})
            return HttpResponse(resp)
    except:
        resp = json.dumps({'check': 'error'})
        return HttpResponse(resp)


def updatewholeplan(request):
    if request.session.has_key('customer'):
        if request.method == "POST":
            p_id=request.POST['plan_id']
            plan=Plans.objects.get(id=p_id)
            plan_price=plan.price
            points=request.user.userdata.points
            amount=float(plan_price)-float(points)
            userdata = UserData.objects.get(user=request.user)
            userdata.payment_uuid = uuid.uuid1().hex
            userdata.plan = plan
            userdata.save()

            try:
                param_dict = {

                    'MID': MERCHANT_ID,
                    'ORDER_ID': str(userdata.payment_uuid),
                    'TXN_AMOUNT': str(amount),
                    'CUST_ID': request.user.email,
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL': 'http://127.0.0.1:8000/wholechange/',

                }
                param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

                return render(request, 'paytm.html', {'param_dict': param_dict})



            except IntegrityError:
                transaction.rollback()
                messages.error(request, "Some Thing Went Wrong")

    return redirect("Home")



@csrf_exempt
@transaction.atomic
def wholechange(request):
    form = request.POST
    response_dict = {}
    checksum = ''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:

        if response_dict['RESPCODE'] == '01':

            payment_uuid=response_dict['ORDERID']
            txn_id = response_dict['TXNID']
            amount = response_dict['TXNAMOUNT']
            udata=UserData.objects.get(payment_uuid=payment_uuid)
            udata.is_chart_sent=False
            udata.dietitian=udata.dietitian
            days_in_month = calendar.monthrange(datetime.today().year, datetime.today().month)[1]
            udata.plan_end_date=datetime.today()+timedelta(days=days_in_month)
            udata.date_tofill_form = datetime.today() + timedelta(days=7)
            udata.call_count=0
            udata.points=0
            udata.plan_buy_count +=1
            udata.is_feed_remain=True
            udata.save()
            payment1 = payment(user_id=udata, transaction_id=txn_id, plan_id=udata.plan,
                               amount=udata.plan.price, date=date.today(), time=datetime.now().strftime("%H:%M:%S"))
            payment1.save()


            msg = f"""   <html><body>
                                   <div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">
                                    
                                       <div class="row" style="margin-left:15%">
                                           <div class="col-12">
                                               <h5 style="color:#6BCCBA;font-size:20px;">Your Plan is Successfully Updated</h5>
                                           </div>
                                       </div>
                                        <div class="row" style="margin-left:15%">
                                               <div class="col-12">
                                                   <h5 style="color:#6BCCBA">Transaction id : {txn_id}</h5>
                                               </div>
                                               <div class="col-12">
                                                   <h5 style="color:#6BCCBA">Transaction Amount : {amount}</h5>
                                               </div></div> 
                                   </body>
                                   </html>
                                               """
            email = EmailMultiAlternatives(
                subject="Plan Update",
                body=msg,
                from_email=MY_SETTING,
                to=[udata.user.email],

            )
            email.mixed_subtype = 'related'

            email.content_subtype = "html"
            email.send()
            response_dict['update_id']=udata.user.id



    return render(request, 'paymentstatus.html', {'response': response_dict,'is_update':True})


def create_room(request, mid):
    if request.method == "GET":
        if request.session.has_key('dietitian'):
            id = mid
            met = meeting.objects.get(id=id)
            name = "Chat with " + met.user.firstname
            room = Room(name=name, created_by=request.user.username, created_at=datetime.today(), meeting=met)
            room.save()
            member = Room_Member(room=room, username=met.user, is_member=True,
                                 added_by=request.user.username)
            member.save()
            met.status = 3
            met.room_id = room.id
            met.save()

            msg = Messages(text="Welcome to SastaDiet Chat I am your Dietitian " + request.user.username,
                           sender=request.user.username, room_id=room)
            msg.save()

            try:
                msg = f"""   <html><body>
                                                   <div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">

                                                       <div class="row" style="margin-left:15%">
                                                           <div class="col-12">
                                                               <h5 style="color:#6BCCBA;font-size:20px;">Your Dietitian has created chat room please join within  2-3 minutes Dietitian is waiting</h5>
                                                           </div>
                                                       </div>

                                                   </body>
                                                   </html>
                                                               """
                email = EmailMultiAlternatives(
                    subject="Chat Room On SastaDiet",
                    body=msg,
                    from_email=MY_SETTING,
                    to=[met.user.user.email],

                )
                email.mixed_subtype = 'related'

                email.content_subtype = "html"
                email.send()
            except:
                pass
            return redirect("http://www.sastadiet.com:9000/ws/join_room/" + str(room.id))


def join_room(request, id):
    if request.session.has_key('dietitian'):
        try:
            room = Room.objects.get(id=id)
            member = Room_Member.objects.get(room=room)
            return render(request, 'chatbot.html', {
                'room_id': mark_safe(json.dumps(id)),
                'room_member': member,

                'userName': mark_safe(json.dumps(request.user.username))
            })
        except:
            return HttpResponse("No Such ROOM")

    if request.session.has_key('customer'):
        try:
            met = meeting.objects.get(room_id=id)
            if met.status == 3:
                room = Room(id=id)

                member = Room_Member.objects.get(room=room, username=request.user.userdata, is_member=True)
                return render(request, 'chatbot.html', {
                    'room_id': mark_safe(json.dumps(id)),
                    'room_member': member,
                    'userName': mark_safe(json.dumps(request.user.username)),
                    'room': room
                })
            else:
                return redirect("userdashboard")
        except:
            return HttpResponse("No Such ROOM")


def end_chat(request, id):
    if request.session.has_key('dietitian'):
        id = id
        room = Room.objects.get(id=id)

        room.meeting.status = 4
        room.meeting.save()

        return redirect('dietitiandashboard')
    return redirect("Home")


def week_report(request):
    if request.method == "POST":
        old_weight = request.POST['old_weight']
        new_weight = request.POST['new_weight']
        query = request.POST.get('query', '')

        request.user.userdata.weight = new_weight
        request.user.userdata.date_tofill_form = datetime.today() + timedelta(days=7)
        request.user.userdata.save()
        report = Week_Report(user=request.user.userdata, old_weight=old_weight, new_weight=new_weight, query=query,
                             date=datetime.today())
        report.save()
        if request.user.userdata.userhealthdata.want_to_achive == "weight-loss":
            if old_weight > new_weight:
                request.session["report_msg"] = 'Congrats , You have lost your weight by ' + str(
                    float(old_weight) - float(new_weight)) + ' kg'
                request.session["achive"] = 'success'
            else:
                request.session["report_msg"] = 'Oops , You have gain your weight by ' + str(
                    float(new_weight) - float(old_weight)) + ' kg'
                request.session["achive"] = 'warning'


        elif request.user.userdata.userhealthdata.want_to_achive == "weight-gain":
            if old_weight > new_weight:
                request.session["report_msg"] = 'Oops , You have lost your weight by ' + str(
                    float(old_weight) - float(new_weight)) + ' kg'
                request.session["achive"] = 'warning'

            else:
                request.session["report_msg"] = 'Congrats , You have gain your weight by ' + str(
                    float(new_weight) - float(old_weight)) + ' kg'
                request.session["achive"] = 'success'

        return redirect("userdashboard")


def changepass(request):
    if request.session.has_key('customer'):
        if request.method == "POST":

            old_pass = request.POST['current_pass']
            print(old_pass)
            print(request.user.password)
            if check_password(old_pass,request.user.password):
                new_pass = request.POST['new_pass']
                request.user.password = make_password(new_pass)
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Your Password is Successfully Change")
            else:
                messages.error(request, "Your Current Password Not matching")

            return redirect('userdashboard')
        return redirect('Home')
    return redirect('Home')


def forgetpassword(request):
    if request.method == "GET":
        email = request.GET["email"]

        user = None
        try:
            user = MyUser.objects.get(email=email)
            if user is None:
                resp = json.dumps({'message': 'You Are Not Member'})
                return HttpResponse(resp)
        except:
            pass
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(8))
        refkey = make_password(result_str)

        uid = str(user.id)

        try:
            email = EmailMessage(
                subject="Forget Password",
                body="https://127.0.0.1:8000/getpassword/?q=" + refkey + "&uid=" + str(
                    uid) + "\n Click On Above Link for Verification",
                from_email=MY_SETTING,
                to=[email],

            )

            email.send()
            user.ref_key = ""
            user.ref_key = result_str
            user.save()
            resp = json.dumps({'message': 'We sent you email with link click on it'})
            return HttpResponse(resp)
        except:
            resp = json.dumps({'message': 'Error'})
            return HttpResponse(resp)

    return redirect("Home")


def getpassword(request):
    if request.method == "POST":
        q = request.POST.get('key', '')
        uid = request.POST.get('uid', '')
        password = request.POST.get('new_pass', '')
        user = MyUser.objects.get(id=uid)

        if check_password(user.ref_key, q):

            user.password = ""
            user.password = make_password(password)
            user.save()
        else:
            messages.error(request, "Error")
            return render(request, "foregt_changepassword.html")
        messages.success(request, "Successfully Changed")
        return render(request, "index.html")
    q = request.GET.get('q', '')
    uid = request.GET.get('uid', '')
    param = {'key': q, 'uid': uid}
    return render(request, "foregt_changepassword.html", param)


def endcall(request, id):
    if request.session.has_key('dietitian'):
        id = id
        try:
            met = meeting.objects.get(id=id)
            met.status = 4
            met.save()
        except:
            messages.error(request, "Something Went Wrong")

        return redirect("dietitiandashboard")


def deletcinactive(request):
    MyUser.objects.filter(is_active=False).delete()
    resp = json.dumps({'msg': 'deleted'})
    return HttpResponse(resp)


def checkmeetingstatus(request):
    id = request.GET['id']

    try:
        room = Room.objects.get(id=id)
        if room:

            resp = json.dumps({'msg': 'success', 'status': room.meeting.status})
            return HttpResponse(resp)
        else:
            resp = json.dumps({'msg': 'fail'})
            return HttpResponse(resp)
    except:
        resp = json.dumps({'msg': 'error'})
        return HttpResponse(resp)
