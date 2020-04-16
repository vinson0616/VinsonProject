from django.shortcuts import render
from django.views.generic.base import View

from .models import Banner


class IndexView(View):
    """
    首页
    """

    def get(self, request):
        # 获取轮播图
        all_banners = Banner.objects.all().order_by('index')
        return render(request, 'index.html', {
            "all_banners": all_banners

        })