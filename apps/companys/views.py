from django.shortcuts import render
from django.views.generic.base import View
from users.models import Navigation
from .models import Company, CompanyHistory, Employee, FriendlyLink

def get_system_info():
    navigations = Navigation.objects.all()[:10]
    system = Company.objects.all().filter(show=True)
    if system:
        system = system.first()
    else:
        system = {}
    return {
        "navigations": navigations,
        "company": system
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