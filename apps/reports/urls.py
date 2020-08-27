from django.urls import path, include,re_path
from .views import ReportView,ReportInfoView




app_name = "reports"

urlpatterns = [
    # 列表
    path('', ReportView.as_view(), name="index"),
    path('info/', ReportInfoView.as_view(), name="info"),

]