from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from companys.views import get_system_info
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib import messages

from .forms import ReportInfoForm
from .models import Report


# Create your views here.
class ReportView(View):
    """
    报名窗口
    """
    def get(self, request):

        return render(request, "report.html", {
            "system": get_system_info()
        })


class ReportInfoView(View):
    """
    资料提交
    """
    def post(self, request):
        msg = ''
        detail = ''
        report_form = ReportInfoForm(request.POST,request.FILES)
        if report_form.is_valid():
            report_form.save(commit=True)
            msg = "提交成功"
            detail = "资料审核通过后，请留意手机短信或者电话."
        else:
            msg = "提交失败"
            detail = "请检查相关的资料是否填写完整, 请点击返回按钮再重试一次!"

        return render(request, "report-result.html", {
            "system": get_system_info(),
            "msg": msg,
            "detail": detail
        })
