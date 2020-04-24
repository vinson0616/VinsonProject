from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class News(models.Model):
    """
    新闻动态
    """
    title = models.CharField(max_length=50, verbose_name="新闻标题")
    content = UEditorField(verbose_name="新闻内容", width=800, height=300, imagePath="news/ueditor/",
                          filePath="news/ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")

    class Meta:
        verbose_name = "新闻动态"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
