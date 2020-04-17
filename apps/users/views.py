from django.shortcuts import render, reverse
from django.views.generic.base import View

from .models import Banner,Navigation
from companys.models import Company, Employee
from products.models import Product
from companys.views import get_system_info
from systems.models import CircleItem


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        # 获取轮播图
        all_banners = Banner.objects.all().order_by('index')
        # 获取产品信息
        products = Product.objects.all().order_by('add_time')[:8]
        # 获取员工信息
        employees = Employee.objects.all()[:5]
        # 获取大圆形内容
        big_circle_items = CircleItem.objects.all().filter(type="big")[:4]
        small_circle_items = CircleItem.objects.all().filter(type="small")[:8]
        return render(request, 'index.html', {
            "all_banners": all_banners,
            "system": get_system_info(),
            "products": products,
            "employees": employees,
            "big_circle_items": big_circle_items,
            "small_circle_items": small_circle_items
        })


