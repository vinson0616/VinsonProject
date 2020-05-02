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
from django.views.static import serve
from VinsonProject.settings import MEDIA_ROOT
import xadmin

from users.views import IndexView

urlpatterns = [
    # 后台管理首页
    path('xadmin/', xadmin.site.urls),

    # 配置上传文件的访问处理函数
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 首页
    path('', IndexView.as_view(), name="index"),

    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),

    # 用户 相关url配置
    path("users/", include('users.urls', namespace="users")),

    # 公司 相关url配置
    path("company/", include('companys.urls', namespace="companys")),

    # 产品 相关url配置
    path("products/", include('products.urls', namespace="products")),

    # 新闻动态 相关url配置
    path("news/", include('news.urls', namespace="news")),

    # 人才招聘 相关url配置
    path("jobs/", include('jobs.urls', namespace="jobs")),
]
