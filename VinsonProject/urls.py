"""VinsonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include,re_path
import xadmin

from users.views import IndexView

urlpatterns = [
    # 后台管理首页
    path('xadmin/', xadmin.site.urls),

    # 首页
    path('', IndexView.as_view(), name="index"),

    # 用户 相关url配置
    path("users/", include('users.urls', namespace="users")),
]
