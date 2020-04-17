from datetime import datetime
from django.db import models


class Company(models.Model):
    """
    公司列表
    """
    company_name = models.CharField(max_length=100, verbose_name="公司名称")
    logo = models.ImageField(upload_to="logo/", null=True, blank=True, verbose_name="公司logo", max_length=100)
    show = models.BooleanField(default=True, verbose_name="是否显示")
    company_desc = models.TextField(verbose_name="公司简述", null=True, blank=True)
    notice_title = models.CharField(max_length=100, verbose_name="宣传标题", default="")
    notice_content = models.TextField(verbose_name="宣传内容", default="")
    footer_desc = models.CharField(max_length=100, verbose_name="底部栏描述", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    """
    员工
    """
    name = models.CharField(max_length=100, verbose_name="姓名")
    image = models.ImageField(upload_to="employee/", null=True, blank=True, verbose_name="头像", max_length=100)
    position = models.CharField(max_length=100, verbose_name="职位", blank=True,null=True)
    desc = models.TextField(verbose_name="描述", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "员工管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CompanyHistory(models.Model):
    """
    公司历史大事
    """
    title = models.CharField(max_length=100, verbose_name="标题")
    desc = models.TextField(verbose_name="描述", null=True, blank=True)
    image = models.ImageField(upload_to="company-history/", null=True, blank=True, verbose_name="图片", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "公司历史"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FriendlyLink(models.Model):
    """
    友情链接
    """
    name = models.CharField(max_length=100, verbose_name="名称")
    logo = models.ImageField(upload_to="friendly/", null=True, blank=True, verbose_name="图片", max_length=100)
    url = models.CharField(max_length=100, null=True, blank=True, verbose_name="地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
