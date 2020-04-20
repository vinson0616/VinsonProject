from django.urls import path, include,re_path
from .views import JobsView



app_name = "jobs"

urlpatterns = [
    # 列表
    path('', JobsView.as_view(), name="index"),

]