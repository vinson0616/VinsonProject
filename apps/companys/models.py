from datetime import datetime
from django.db import models


class Company(models.Model):
    """
    公司列表
    """
    company_name = models.CharField(max_length=100, verbose_name="公司名称")
    logo = models.ImageField(upload_to="logo/", null=True, blank=True, verbose_name="头部公司logo", max_length=100)
    footer_logo = models.ImageField(upload_to="logo/", null=True, blank=True, verbose_name="底部公司logo", max_length=100)
    show = models.BooleanField(default=True, verbose_name="是否显示")
    company_desc = models.TextField(verbose_name="公司简述", null=True, blank=True)
    notice_title = models.CharField(max_length=100, verbose_name="宣传标题", default="")
    notice_content = models.TextField(verbose_name="宣传内容", default="")
    footer_desc = models.CharField(max_length=100, verbose_name="底部栏描述", null=True, blank=True)
    address_province = models.CharField(max_length=200, verbose_name="省市区", null=True, blank=True)
    address_street = models.CharField(max_length=200, verbose_name="街道楼号", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="联系电话", null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name="Email", null=True, blank=True)
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


class UserMessage(models.Model):
    """
    在线留言
    """
    name = models.CharField(max_length=20, verbose_name="姓名", null=True, blank=True)
    title = models.CharField(max_length=30, verbose_name="标题", null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name="手机")
    email =  models.CharField(max_length=30, verbose_name="电子邮件", null=True, blank=True)
    content = models.TextField(verbose_name="内容", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "在线留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
