from django.urls import path, include,re_path
from .views import NewsListView, NewsDetailView


app_name = "news"

urlpatterns = [
    # 列表
    path('list/', NewsListView.as_view(), name="list"),
    # # 详情页面
    re_path('detail/(?P<news_id>\d+)/', NewsDetailView.as_view(), name="detail"),
]