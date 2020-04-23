from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from users.models import Navigation
from .models import Company, CompanyHistory, Employee, FriendlyLink
from news.models import News
from products.models import Product
from .forms import UserMessageForm

def get_system_info():
    navigations = Navigation.objects.all()[:10]
    system = Company.objects.all().filter(show=True)
    news = News.objects.all().order_by("-add_time")[:3]
    products = Product.objects.all().order_by("-add_time")[:3]
    if system:
        system = system.first()
    else:
        system = {}
    return {
        "navigations": navigations,
        "company": system,
        "news": news,
        "products": products
    }


class AboutView(View):
    """
    关于我们
    """
    def get(self, request):

        company_histories = CompanyHistory.objects.all()
        employees = Employee.objects.all()[:4]
        friendly_links = FriendlyLink.objects.all()[:10]
        return render(request,"about.html",{
            "company_histories": company_histories,
            "system": get_system_info(),
            "employees": employees,
            "friendly_links": friendly_links
        })


class ContactMeView(View):
    def get(self, request):
        return render(request, "contact-me.html",{
            "system": get_system_info(),
        })


class UserMessageView(View):
    """
    用户在线留言
    """
    def post(self, request):
        userMessage_form = UserMessageForm(request.POST)
        if userMessage_form.is_valid():
            user_message = userMessage_form.save(commit=True)
            # 异步返回操作，也就是局部刷新
            return HttpResponse('{"status":"success"}',
                                content_type='application/json')
        else:
            return HttpResponse(
                '{"status":"fail", "msg":"添加失败"}',
                content_type='application/json')
