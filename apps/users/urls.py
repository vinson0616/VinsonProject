from django.urls import path, include,re_path
from .views import LoginView, LogoutView, RegisterView
from .views import UserInfoView

app_name = "users"

urlpatterns = [
    # 用户信息
    path('login/', LoginView.as_view(), name="login"),
    # 退出登录
    path('logout/', LogoutView.as_view(), name="logout"),
    # 注册
    path('register/', RegisterView.as_view(), name="register"),
    # 个人中心- 我的信息
    path('info/', UserInfoView.as_view(), name="usercenter-info"),
]