from django.urls import path, include,re_path
from .views import LibraryDetailView, LibraryListView

app_name = "library"

urlpatterns = [
    # 列表
    #path('list/', ProductListView.as_view(), name="list"),
    # 详情页面
    re_path('detail/(?P<library_id>\d+)/', LibraryDetailView.as_view(), name="detail"),
    # 资源素材列表
    path('list/', LibraryListView.as_view(), name="list")
]