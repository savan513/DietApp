import uuid

from django.db import models
from django import forms
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import datetime


# Create your models here.
class MyManager(BaseUserManager):

    def create_user(self, username, email, is_customer=True, is_dietitian=False, password=None,is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            username=username
        )

        user.set_password(password)  # change password to hash
        user.is_sho = False
        user.email = email
        user.is_admin = False
        user.is_dietitian = is_dietitian
        user.is_customer = is_customer
        user.is_staff = False
        user.is_active = is_active
        user.ref_key=make_password(user.id)
        return user

    def save(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)  # change password to hash

        user.is_admin = False
        user.is_dietitian = False
        user.is_customer = True
        user.is_staff = False
        user.is_active = True

        return user

    def create_superuser(self, username, password, email):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.email = email
        user.is_admin = True
        user.is_customer = False
        user.is_dietitian = False
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.ref_key = make_password(user.id)
        user.save(using=self._db)
        return user




# Create your models here.
class MyUser(AbstractBaseUser,PermissionsMixin):
    class Meta:
        verbose_name_plural = "Authentication"


    id = models.AutoField(primary_key=True)
    email = models.EmailField(('email address'),unique=True,null=True,default="",blank=True)
    username=models.CharField(default="",max_length=15,unique=True)
    is_customer = models.BooleanField(default=False)
    is_dietitian = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    ref_key = models.CharField(default="", max_length=100, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = MyManager()

    def __str__(self):
        return self.username

class dietitian(models.Model):
    user = models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    firstname = models.CharField(default="", max_length=10)
    middlename = models.CharField(default="", max_length=10)
    lastname = models.CharField(default="", max_length=10)
    mobile_no = models.CharField(max_length=10, default="")
    qualification = models.CharField(max_length=10, default="")
    image=models.ImageField(upload_to='diet_app')
    commission_smartplan = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    commission_smartplan_healthissue = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    commission_smartplusplan = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    commission_smartplusplan_healthissue = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    revenue=models.DecimalField(default=0.0,max_digits = 5, decimal_places=2,blank=True,null=True)
    def __str__(self):
        return self.firstname

class Plans(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=300,default="")
    price=models.FloatField(default="")
    is_plusplan=models.BooleanField(default=False)
    is_healthissue=models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def split_description(self):
        return self.description.split(',')

class UserData(models.Model):

    class Meta:
        verbose_name_plural = "Cutomers"

    user= models.OneToOneField(
        MyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    firstname=models.CharField(default="",max_length=10)
    middlename=models.CharField(default="",max_length=10)
    lastname=models.CharField(default="",max_length=10)
    age= models.IntegerField(null=True, blank=True,default=10)
    gender=models.CharField(default="",max_length=11)
    height= models.DecimalField(default=0.0,max_digits = 5, decimal_places=2)
    weight=models.DecimalField(default=0.0,max_digits = 5, decimal_places=2)
    mobile_no=models.CharField(max_length=10,default="")
    city=models.CharField(max_length=500,default="")
    created_at = models.DateField(auto_now_add=True, null=True)
    updates_at = models.DateField(null=True)
    date_tofill_form= models.DateField(null=True,blank=True)

    dietitian=models.ForeignKey(dietitian,null=True,blank=True,unique=False,on_delete=models.CASCADE)
    plan=models.ForeignKey(Plans,blank=True,null=True,unique=False,on_delete=models.CASCADE)
    plan_end_date=models.DateField(null=True,blank=True)
    call_count=models.IntegerField(default=0,blank=True,null=True)
    is_data_filled=models.BooleanField(default=False)
    is_chart_sent=models.BooleanField(default=False)
    payment_uuid = models.CharField(default=uuid.uuid1, max_length=200,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    referral_code=models.CharField(default="",max_length=100)
    points=models.DecimalField(default=0.0,max_digits = 5, decimal_places=2)
    plan_buy_count=models.IntegerField(default=1,blank=True)
    is_feed_remain=models.BooleanField(default=True)



    def __str__(self):
        if self.firstname:
            return self.firstname
        else:
            return self.user.username
    def is_expired(self):
        self.user.is_active=False
        return datetime.datetime.today().date() >= self.plan_end_date
    def is_week(self):
        delta =  self.date_tofill_form - datetime.datetime.today().date()

        if delta.days < 3:
            return True
        else:
            return False

    def is_last_Day(self):

        delta= self.plan_end_date - datetime.datetime.today().date()

        if delta.days == 1:

            return True
        else:
            return False

class Week_Report(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserData,on_delete=models.CASCADE)
    old_weight=models.DecimalField(default=0.0,max_digits=5, decimal_places=2)
    new_weight = models.DecimalField(null=True, blank=True, default=0.0, max_digits=5, decimal_places=2)
    query=models.CharField(max_length=400,default="")
    date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.user.firstname


class UserHealthData(models.Model):
    class Meta:
        verbose_name_plural = "Cutomer's Health Data"

    userdata=models.OneToOneField(UserData,on_delete=models.CASCADE,primary_key=True)
    workout=models.BooleanField(default=False)

    workout_time=models.CharField(default="",max_length=15)
    workout_time_inday=models.CharField(default="",max_length=20)
    workout_day_inweek=models.CharField(default="",max_length=20)
    want_to_achive=models.CharField(default="",max_length=30)
    type=models.CharField(default="",max_length=30)
    dishes=models.CharField(default="",max_length=30)
    have_disease=models.BooleanField(default=False)
    supplements=models.CharField(default="",max_length=200)
    about=models.CharField(default="",max_length=300)

    def __str__(self):
        return self.userdata.user.username

    def workout_type(self):
        types = Workout_type.objects.filter(user=self)
        typelist = []
        for t in types:
            typelist.append(t.type)
        return typelist



class Workout_type(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(default="",max_length=20)
    user=models.ForeignKey(UserHealthData,on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(default="",max_length=20)
    email=models.CharField(default="",max_length=50)
    subject=models.CharField(default="",max_length=50)
    message=models.CharField(default="",max_length=300)

    def __str__(self):
        return self.email

class meeting(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserData,on_delete=models.CASCADE)
    dietitian=models.ForeignKey(dietitian,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.date.today)
    time=models.TimeField(auto_now=False, auto_now_add=False,default=datetime.datetime.now())
    end_time=models.TimeField(auto_now=False, auto_now_add=False,default=datetime.datetime.now())
    status=models.IntegerField(default=0)
    created_at=models.DateField()
    updated_at=models.DateField()
    type=models.CharField(max_length=70,default="")
    room_id=models.IntegerField(blank=True,null=True)


    def __str__(self):
        return str(self.id)

class Room(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="")
    created_by=models.CharField(max_length=100,default="")
    created_at=models.DateField(null=True)
    meeting=models.ForeignKey(meeting,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Messages(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.CharField(max_length=500,default="")
    sender=models.CharField(max_length=100,default="")
    room_id=models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return self.sender


class Room_Member(models.Model):
    id=models.AutoField(primary_key=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,unique=False)
    username=models.ForeignKey(UserData,on_delete=models.CASCADE,unique=False)
    is_member=models.BooleanField(default=False)
    added_by=models.CharField(max_length=40,default="")

    def __str__(self):
        return self.username.firstname



class payment(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(UserData,on_delete=models.CASCADE)
    transaction_id=models.CharField(default="",max_length=200)
    plan_id=models.ForeignKey(Plans,on_delete=models.PROTECT)
    amount=models.DecimalField(default=0.0,max_digits = 5, decimal_places=2)
    date=models.DateField(default=datetime.datetime.today())
    time = models.TimeField(default=datetime.datetime.now().time())

    def __str__(self):
        return self.transaction_id

class poster(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='diet_app')
    name=models.CharField(default="",max_length=30)

    def __str__(self):
        return str(self.image)

class feedback(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(default="",max_length=50)
    review=models.CharField(default="",max_length=300)
    datetime=models.DateTimeField(default=datetime.datetime.today())
    image=models.ImageField(default='/diet_app/avatar.png/',upload_to='diet_app')
    def __str__(self):
        return self.name

