from django.urls import path, include,re_path
from .views import AboutView

app_name = "companys"

urlpatterns = [
    # 关于我们
    path('about/', AboutView.as_view(), name="about"),
]