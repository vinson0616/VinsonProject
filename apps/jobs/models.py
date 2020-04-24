from datetime import datetime
from django.db import models


class Position(models.Model):
    """
    新闻动态
    """
    name = models.CharField(max_length=100, verbose_name="招聘职位")
    desc = models.TextField(verbose_name="岗位描述", null=True, blank=True)
    detail = models.TextField(verbose_name="相关要求", null=True, blank=True)
    show = models.BooleanField(verbose_name="是否显示", max_length=5, default=True)
    mobile = models.CharField(verbose_name="联系电话", max_length=20, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")

    class Meta:
        verbose_name = "职位发布"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name