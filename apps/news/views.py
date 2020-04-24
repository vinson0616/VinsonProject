from django.shortcuts import render
from django.views.generic.base import View
from .models import News
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from companys.views import get_system_info


class NewsListView(View):

    def get(self,request):
        all_news = News.objects.all().order_by("-add_time")
        total = all_news.count()
        # 对课程进行分页显示
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_news, 20, request=request)
        all_news = p.page(page)

        return render(request,"news-list.html", {
            "system": get_system_info(),
            "all_news": all_news,
            "total": total
        })


class NewsDetailView(View):
    """
    新闻动态 详细信息
    """
    def get(self, request, news_id):
        news = News.objects.get(id=int(news_id))

        return render(request, "news-detail.html", {
            "system": get_system_info(),
            "news": news
        })

