import xadmin
from xadmin import views

from django.contrib.auth.models import Group, Permission
from xadmin.models import Log

from .models import UserProfile, Banner, Navigation
from companys.models import Company, Employee, CompanyHistory, FriendlyLink
from products.models import ProductCategory, Product
from systems.models import CircleItem
from news.models import News


class BaseSetting(object):
    enable_themes = True  #主题开启
    use_bootswatch = True  #主题开启


class GlobalSettings(object):
    site_title = "Vinson模板管理系统"  #页面左上角
    site_footer = "2020 Vinson模板管理系统"
    # menu_style = "accordion"

    def get_site_menu(self):
        return (
            {'title': '产品管理', 'menus': (
                {'title': '产品类别', 'url': self.get_model_url(ProductCategory, 'changelist')},
                {'title': '产品信息', 'url': self.get_model_url(Product, 'changelist')},
            )},
            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
            )},
            {'title': '公司管理', 'menus': (
                {'title': '公司列表', 'url': self.get_model_url(Company, 'changelist')},
                {'title': '公司大事记', 'url': self.get_model_url(CompanyHistory, 'changelist')},
                {'title': '员工管理', 'url': self.get_model_url(Employee, 'changelist')},
                {'title': '新闻动态', 'url': self.get_model_url(News, 'changelist')},
                {'title': '友情链接', 'url': self.get_model_url(FriendlyLink, 'changelist')},
            )},
            {'title': '首页内容', 'menus': (
                {'title': '导航栏', 'url': self.get_model_url(Navigation, 'changelist')},
                {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '圆形内容', 'url': self.get_model_url(CircleItem, 'changelist')},
            )},
            {'title': '系统管理', 'menus': (
                {'title': '权限分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},
        )


class BannerAdmin(object):
    list_display = ['title', 'show_button', 'image', 'index', 'add_time']
    search_fields = ['title', 'show_button', 'image', 'index']
    list_filter = ['title', 'show_button', 'image', 'index', 'add_time']
    readonly_fields = ['add_time']


class CompanyAdmin(object):
    list_display = ['company_name', 'show', 'add_time']
    search_fields = ['company_name', 'show', 'add_time']
    list_filter = ['company_name', 'show', 'add_time']
    readonly_fields = ['add_time']


class ProductCategoryAdmin(object):
    list_display = ['name', 'parent_category', 'add_time']
    search_fields = ['name', 'parent_category', 'add_time']
    list_filter = ['name', 'parent_category', 'add_time']
    readonly_fields = ['add_time']


class ProductAdmin(object):
    list_display = ['name', 'category', 'add_time']
    search_fields = ['name', 'category', 'add_time']
    list_filter = ['name', 'category', 'add_time']
    readonly_fields = ['add_time']


class EmployeeAdmin(object):
    list_display = ['name', 'position', 'add_time']
    search_fields = ['name', 'position', 'add_time']
    list_filter = ['name', 'position', 'add_time']
    readonly_fields = ['add_time']


class NavigationAdmin(object):
    list_display = ['name', 'url', 'add_time']
    search_fields = ['name', 'url', 'add_time']
    list_filter = ['name', 'url', 'add_time']
    readonly_fields = ['add_time']


class CircleItemAdmin(object):
    list_display = ['title', 'type', 'icon','url', 'add_time']
    search_fields = ['title', 'url', 'add_time']
    list_filter = ['title', 'url', 'add_time']
    readonly_fields = ['add_time']


class CompanyHistoryAdmin(object):
    list_display = ['title', 'desc',  'add_time']
    search_fields = ['title', 'desc', 'add_time']
    list_filter = ['title', 'desc', 'add_time']
    readonly_fields = ['add_time']


class FriendlyLinkAdmin(object):
    list_display = ['name', 'url',  'add_time']
    search_fields = ['name', 'url', 'add_time']
    list_filter = ['name', 'url', 'add_time']
    readonly_fields = ['add_time']


class NewsAdmin(object):
    list_display = ['title',  'add_time']
    search_fields = ['title',  'add_time']
    list_filter = ['title', 'add_time']
    readonly_fields = ['add_time']


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(ProductCategory, ProductCategoryAdmin)
xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Employee, EmployeeAdmin)
xadmin.site.register(Navigation, NavigationAdmin)
xadmin.site.register(CircleItem, CircleItemAdmin)
xadmin.site.register(CompanyHistory, CompanyHistoryAdmin)
xadmin.site.register(FriendlyLink, FriendlyLinkAdmin)
xadmin.site.register(News, NewsAdmin)