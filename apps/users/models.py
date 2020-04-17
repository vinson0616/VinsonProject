from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="female")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    image = models.ImageField(upload_to="image/%Y/%m", null=True, blank=True, default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Banner(models.Model):
    """
    首页轮播图
    """
    title = models.CharField(max_length=100, verbose_name="标题")
    desc_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="描述1")
    desc_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="描述2")
    desc_3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="描述3")
    show_button = models.BooleanField(default=True, verbose_name="是否显示按钮")
    index = models.IntegerField(default=1, verbose_name="显示顺序")
    image = models.ImageField(upload_to="banner/%Y/%m", null=True, blank=True, verbose_name="轮播图", max_length=100)
    add_time = models.DateTimeField(default = datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Navigation(models.Model):
    """
    导航栏
    """
    name = models.CharField(max_length=100, verbose_name="名称")
    url = models.CharField(max_length=100, verbose_name="Url")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "导航栏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



