from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


class ProductCategory(models.Model):
    """
    产品类别
    """
    name = models.CharField(default="", max_length=50, verbose_name="类别名称")
    desc = models.CharField(default="", null=True, blank=True,max_length=300, verbose_name="类别描述")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别级别", help_text="父目录",
                                      on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "产品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_category_by_parent(self):
        return ProductCategory.objects.filter(parent_category=self.id)


class Product(models.Model):
    """
    产品
    """
    category = models.ForeignKey(ProductCategory, verbose_name="产品类别", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="产品名称")
    image = models.ImageField(upload_to="products/", verbose_name="图片", blank=True, null=True, max_length=100)
    detail = UEditorField(verbose_name="产品介绍", width=800, height=300, imagePath="products/ueditor/",
                          filePath="products/ueditor/", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CompanyLink(models.Model):
    """
    公司环节
    """
    name = models.CharField(max_length=50, verbose_name="产品名称")
    image = models.ImageField(upload_to="products/", verbose_name="图片", blank=True, null=True, max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "公司环节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name