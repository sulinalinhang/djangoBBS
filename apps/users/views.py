from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import UserProfile, EmailVerifyRecord


class CustomBackend(ModelBackend):
    @classmethod
    def authenticate(cls, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})


class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = CustomBackend.authenticate(username=user_name, password=pass_word)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # print('进来了111111111111111111111111111')
                    return redirect('../mytopic/')
                else:
                    return render(request, "index.html", {"msg":"用户未激活！"})
            else:
                return render(request, "index.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "index.html", {"login_form":login_form})


class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username", "")
            if UserProfile.objects.filter(username=user_name):
                return render(request, "index.html", {"msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = True
            user_profile.password = make_password(pass_word)
            user_profile.save()

            #写入欢迎注册消息
            # user_message = UserMessage()
            # user_message.user = user_profile.id
            # user_message.message = "欢迎注册慕学在线网"
            # user_message.save()

            # send_register_email(user_name, "register")
            return render(request, "index.html")
        else:
            return render(request, "index.html", {"msg":'请输入正确用户名和密码'})