from datetime import datetime
from django.db import models


# 素材库类别
class LibraryCategory(models.Model):
    name = models.CharField(default="", max_length=50, verbose_name="类别名称")
    desc = models.CharField(default="", null=True, blank=True,max_length=300, verbose_name="类别描述")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别级别", help_text="父目录",
                                      on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "素材库类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_category_by_parent(self):
        return LibraryCategory.objects.filter(parent_category=self.id)


# 素材资源
class LibraryMedia(models.Model):
    category = models.ForeignKey(LibraryCategory, verbose_name="类别", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="素材名称")
    image = models.ImageField(upload_to="library/image", default='image/question_defalt.jpg', verbose_name="封面图", blank=True, null=True, max_length=100)
    download = models.FileField(upload_to="library/resource",null=True, blank=True, verbose_name="资源文件", max_length=500)
    url = models.CharField(max_length=500, verbose_name="下载链接", null=True, blank=True)
    format= models.CharField(max_length=30, verbose_name="文件格式", null=True, blank=True)
    size = models.DecimalField(verbose_name="文件大小(MB)",max_digits=10, decimal_places=2, default=0.00)
    has_display = models.BooleanField(verbose_name="首页显示", default=False)
    price = models.IntegerField(default=0, verbose_name="价格")
    discount = models.IntegerField(default=100, verbose_name="折扣")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    desc = models.CharField(max_length=200, verbose_name="素材描述", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "素材"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 计算折扣价格
    def get_discount_price(self):
        return self.price*(self.discount/100)