from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import LibraryMedia, LibraryCategory
from companys.views import get_system_info


# Create your views here.
class LibraryDetailView(View):
    """
    资源素材详细信息
    """
    def get(self, request, library_id):
        libraries = LibraryMedia.objects.all().order_by('-add_time')[:5]
        library = LibraryMedia.objects.get(id=int(library_id))
        library.click_nums += 1
        library.save()

        return render(request, "library-detail.html", {
            "system": get_system_info(),
            "library": library,
            "libraries": libraries
        })


class LibraryListView(View):
    """
    资源素材列表
    """
    def get(self, request):

        searchContent = request.GET.get('searchContent')

        # 获取素材库的类别
        all_categories = LibraryCategory.objects.all()
        parent_categories = all_categories.filter(parent_category__isnull=True)
        child_categories = all_categories.filter(parent_category__isnull=False)
        second_categories = []
        third_categories = []
        for category in child_categories:
            parent = LibraryCategory.objects.get(id=category.parent_category.id)
            if parent and parent.parent_category:
                third_categories.append(category)
            else:
                second_categories.append(category)

        # 获取所有章节数据
        all_libraryMedias = LibraryMedia.objects.all().order_by("-add_time")

        # 一级类别过滤
        p_id = int(request.GET.get('p_id', -1))
        c_id = int(request.GET.get('c_id', -1))
        s_id = int(request.GET.get('s_id', -1))
        if p_id != -1:
            # 获取二级目录
            p_parent_categories = child_categories.filter(parent_category_id=p_id)
            second_categories = p_parent_categories
            third_categories = child_categories.filter(parent_category_id__in=second_categories)
            second_third_categories = second_categories | third_categories
            all_libraryMedias = all_libraryMedias.filter(category__in=second_third_categories)

        # 二级类别过滤
        if c_id != -1:
            c_second_categories = child_categories.filter(id=c_id)
            third_categories = child_categories.filter(parent_category_id__in=c_second_categories)
            if c_second_categories:
                # 获取三级的类别
                c_third_categoires = child_categories.filter(parent_category_id=c_id)
                c_third_categoires = c_third_categoires | c_second_categories
                all_libraryMedias = all_libraryMedias.filter(category__in=c_third_categoires)

        # 三级目录过滤
        if s_id != -1:
            all_libraryMedias = all_libraryMedias.filter(category__id=s_id)

        # 搜索
        if searchContent:
            all_libraryMedias = all_libraryMedias.filter(name__icontains=searchContent)
        # 对课程进行分页显示
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_libraryMedias, 12, request=request)
        libraryMedias = p.page(page)

        return render(request, "library-list.html", {
            "all_libraryMedias": libraryMedias,
            "system": get_system_info(),
            "parent_categories": parent_categories,
            "second_categories": second_categories,
            "third_categories": third_categories,
            "p_id": p_id,
            "c_id": c_id,
            "s_id": s_id
        })