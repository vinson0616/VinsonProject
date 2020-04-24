from django.shortcuts import render
from django.views.generic.base import View

from companys.views import get_system_info

from .models import Position


class JobsView(View):
    """
    人才招聘
    """
    def get(self, request):

        all_positions = Position.objects.all().filter(show=True).order_by("-add_time")
        return render(request, "jobs.html", {
            "system": get_system_info(),
            "all_positions": all_positions
        })
