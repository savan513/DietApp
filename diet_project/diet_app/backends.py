from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from .models import MyUser

class UserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            myuser = MyUser.objects.get(username=username)


            if password == myuser.password:

                return myuser
        except :
            pass