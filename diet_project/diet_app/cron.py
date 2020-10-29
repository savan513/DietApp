from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from .models import MyUser
from datetime import datetime
from datetime import timedelta
from django.core.mail import send_mail,EmailMessage,EmailMultiAlternatives
from .app_settings import MY_SETTING
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2


    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'  # a unique code

    def do(self):
        days= timedelta(days=1)
        todays_date=datetime.today()
        match_day=todays_date-days
        user_emails=MyUser.objects.values('email').filter(userdata__plan_end_date= match_day)
        image_name = 'logo.jpeg'
        with open(finders.find('images/logo.jpeg'), 'rb') as f:
            logo_data = f.read()
            logo = MIMEImage(logo_data)
            logo.add_header('Content-ID', f"<{image_name}>")

        msg = f"""       
                        <html><body>
        <div class="container" style="margin-top:15%;border:2px solid #6BCCBA;border-radius:5px;">
         <div class="col my-4" style="margin-top:60px !important;margin-left:15%" >
                    <div class="center">
                        <img src='cid:{image_name}' style="width:50%">
                    </div>
            </div>
            <div class="row" style="margin-left:15%">
                <div class="col-12">
                    <h5 style="color:#6BCCBA;font-size:20px;">Dear Customer Your Diet Plan on SastaDiet will expire soon
    </h5>
                </div>
            </div>
           </div>
        </body>
        </html>
                    """
        email = EmailMultiAlternatives(
            subject="Welcome to Sastadiet",
            body=msg,
            from_email=MY_SETTING,
            to=[user_emails],

        )
        email.mixed_subtype = 'related'
        email.attach(logo)
        email.content_subtype = "html"
        email.send()
