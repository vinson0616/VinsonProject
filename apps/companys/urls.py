from django.urls import path, include,re_path
from .views import AboutView, ContactMeView

app_name = "companys"

urlpatterns = [
    # 关于我们
    path('about/', AboutView.as_view(), name="about"),
    # 联系我们
    path('contact/', ContactMeView.as_view(), name="contact"),
]