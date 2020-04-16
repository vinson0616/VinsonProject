from django.shortcuts import render
from django.views.generic.base import View

from .models import Banner, SystemSetting


class IndexView(View):
    """
    首页
    """

    def get(self, request):
        # 获取轮播图
        all_banners = Banner.objects.all().order_by('index')
        system = SystemSetting.objects.all().filter(show=True)
        if system:
            system = system.first()
        return render(request, 'index.html', {
            "all_banners": all_banners,
            "system": system
        })