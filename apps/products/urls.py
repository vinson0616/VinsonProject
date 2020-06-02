from django.urls import path, include,re_path
from .views import ProductListView, ProductDetailView,CompanyLinkListView

app_name = "products"

urlpatterns = [
    # 列表
    path('list/', ProductListView.as_view(), name="list"),
    # 详情页面
    re_path('detail/(?P<product_id>\d+)/', ProductDetailView.as_view(), name="detail"),
    # 公司环节
    path('companylink/', CompanyLinkListView.as_view(), name="companylink"),
]