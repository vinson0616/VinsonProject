from datetime import datetime
from django.db import models


class CircleItem(models.Model):
    """
    首页中圆形项目内容展示
    """
    title = models.CharField(max_length=100, verbose_name="标题")
    desc = models.TextField(verbose_name="简述", null=True, blank=True)
    icon = models.ImageField(upload_to="icon/", null=True, blank=True, verbose_name="图标", max_length=100)
    url = models.CharField(max_length=200, verbose_name="链接地址", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "圆形内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
