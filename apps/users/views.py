import re
from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password

from .models import Banner,Navigation
from companys.views import get_system_info
from systems.models import CircleItem
from library.models import LibraryMedia, LibraryCategory
from .forms import LoginForm, RegisterForm
from .models import UserProfile


class CustomBackend(ModelBackend):
    """
    实现用户名邮箱均可登录
    继承ModelBackend类，因为它有方法authenticate，可点进源码查看
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        #完成自己的自定义登录逻辑
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
        return None


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        # 获取轮播图
        all_banners = Banner.objects.all().order_by('index')
        # 获取产品信息
        libraries = LibraryMedia.objects.filter(has_display=True).order_by('-add_time')[:6]
        # 获取每个模块的相关信息
        LibraryCategory.objects.all()[:6]
        # 获取圆形内容
        circle_items = CircleItem.objects.all()
        return render(request, 'index.html', {
            "all_banners": all_banners,
            "system": get_system_info(),
            "circle_items": circle_items,
            "libraries": libraries
        })


class LoginView(View):
    """
    登录页面
    """
    def get(self, request):
        return render(request, 'login.html', {
            "system": get_system_info()
        })

    def post(self, request):
        login_form = LoginForm(request.POST)  # 预加载进行校验
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！","system": get_system_info()})
        else:
            return render(request, "login.html", {"login_form": login_form,"system": get_system_info()})


class LogoutView(View):
    """
    退出登录
    """

    def get(self, request):
        logout(request)
        # 完成重定向URL
        return HttpResponseRedirect(reverse('index'))


class RegisterView(View):
    """
    用户注册
    """

    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {
            "register_form": register_form,
            "system": get_system_info()
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username", "")
            if UserProfile.objects.filter(mobile=user_name):
                return render(request, "register.html", {"register_form":register_form, "msg": "用户已经存在","system": get_system_info()})
            password = request.POST.get("password", "")
            password2 = request.POST.get("password2", "")
            if password != password2:
                return render(request, "register.html", {"register_form":register_form, "msg": "两次输入密码不一致","system": get_system_info()})
            # 由于手机号位数大于11位也能匹配成功，所以修改如下：
            ret = re.match(r"^1[35678]\d{9}$", user_name)

            if ret:
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.mobile = user_name
                user_profile.is_active = True
                user_profile.is_staff = True
                user_profile.password = make_password(password)
                user_profile.save()

                user = authenticate(username=user_name, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, "register.html",
                              {"register_form": register_form, "msg": "手机号码格式不正确", "system": get_system_info()})

        return render(request,"register.html", {"register_form": register_form,"system": get_system_info()})


