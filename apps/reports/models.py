from django.db import models
from datetime import datetime


# Create your models here.
class Report(models.Model):
    """
    报名窗口
    """
    name = models.CharField(max_length=100, verbose_name="姓名")
    phone = models.CharField(max_length=11, verbose_name="电话")
    address = models.CharField(max_length=200, verbose_name="地址")
    school = models.CharField(max_length=100, verbose_name="所报学校")
    major = models.CharField(max_length=100, verbose_name="所报专业")
    type = models.IntegerField(default=0,verbose_name="报考类型", choices=((0, "自考"), (1, "成教"),(2, "国开")))
    identity_card1 = models.ImageField(upload_to="identityCard/", default='', verbose_name="身份证正面",
                              blank=True, null=True, max_length=200)
    identity_card2 = models.ImageField(upload_to="identityCard/", default='', verbose_name="身份证背面",
                                       blank=True, null=True, max_length=200)
    graduate_photo = models.ImageField(upload_to="graduate/", default='', verbose_name="毕业证",
                                       blank=True, null=True, max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")

    class Meta:
        verbose_name = "报名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name