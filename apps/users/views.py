from django.shortcuts import render, reverse
from django.views.generic.base import View

from .models import Banner,Navigation
from companys.models import Company, Employee
from products.models import Product,CompanyLink
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
        products = CompanyLink.objects.all().order_by('add_time')[:6]
        # 获取员工信息
        employees = Employee.objects.all()[:5]
        # 获取圆形内容
        circle_items = CircleItem.objects.all()
        return render(request, 'index.html', {
            "all_banners": all_banners,
            "system": get_system_info(),
            "products": products,
            "employees": employees,
            "circle_items": circle_items
        })


