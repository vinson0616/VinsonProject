from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from companys.views import get_system_info

from .models import Product, ProductCategory


class ProductListView(View):
    """
    产品列表页面
    """
    def get(self, request):

        products = Product.objects.all()
        # 获取类型
        all_categories = ProductCategory.objects.all()
        parent_categories = all_categories.filter(parent_category__isnull=True)
        child_categories = all_categories.filter(parent_category__isnull=False)
        second_categories = []
        third_categories = []
        for category in child_categories:
            parent = ProductCategory.objects.get(id=category.parent_category.id)
            if parent and parent.parent_category:
                third_categories.append(category)
            else:
                second_categories.append(category)

        # 一级类别过滤
        p_id = int(request.GET.get('p_id', -1))
        c_id = int(request.GET.get('c_id', -1))

        if p_id != -1:
            # 获取二级目录
            p_parent_categories = child_categories.filter(parent_category_id=p_id)
            second_categories = p_parent_categories
            third_categories = child_categories.filter(parent_category_id__in=second_categories)
            second_third_categories = second_categories | third_categories
            products = products.filter(category__in=second_third_categories)

            # 二级类别过滤
        if c_id != -1:
            c_second_categories = child_categories.filter(id=c_id)
            if c_second_categories:
                # 获取三级的类别
                c_third_categoires = child_categories.filter(parent_category_id=c_id)
                c_third_categoires = c_third_categoires | c_second_categories
                products = products.filter(category__in=c_third_categoires)

        total = products.count()

        # 对课程进行分页显示
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(products, 3, request=request)
        products = p.page(page)

        return render(request, "products-list.html", {
            "system": get_system_info(),
            "products": products,
            "parent_categories": parent_categories,
            "child_categories": second_categories,
            "total": total,
            "p_id": p_id,
            "c_id": c_id
        })


class ProductDetailView(View):
    """
    产品列表页面
    """
    def get(self, request, product_id):
        product = Product.objects.get(id=int(product_id))

        return render(request, "products-detail.html", {
            "system": get_system_info(),
            "product": product
        })