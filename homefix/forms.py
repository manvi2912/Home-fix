from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from homefix.models import *

class registerForm(forms.Form):
    firstname = forms.CharField(max_length=256)
    lastname = forms.CharField(max_length=256)
    email = forms.CharField(max_length=256)
    username = forms.CharField(max_length=256)
    psw = forms.CharField(max_length=256)
    psw_repeat = forms.CharField(max_length=256)

    def check_password(self):
        password = self.cleaned_data['psw']
        confirm_password = self.cleaned_data['psw_repeat']
        if password == confirm_password:
            return True
        return False

    def validate_password(self):
        password = self.cleaned_data['psw']
        if len(password) < 4:
            return False
        return True


    def username_unique(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            return False
        return True

    def email_unique(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            return False
        return True

    def create_user(self):
        username = self.cleaned_data['username']
        psw = self.cleaned_data['psw']
        email = self.cleaned_data['email']
        firstname = self.cleaned_data['firstname']
        lastname = self.cleaned_data['lastname']

        user = User.objects.create_user(username=username, password=psw, first_name = firstname, last_name = lastname, email = email)

        user.save()

        return user

class loginForm(forms.Form):
    username = forms.CharField(max_length=256)
    psw = forms.CharField(max_length=256)

    def verify_and_login(self, request):
        username = self.cleaned_data['username']
        psw = self.cleaned_data['psw']
        user = authenticate(request, username=username, password=psw)
        if user is not None:
            user_type = User_type.objects.get(user=user)
            if  user_type.user_type == 1:
                login(request,user)
                return True
            else:
                return False
        else:
            return False
        
    

    
