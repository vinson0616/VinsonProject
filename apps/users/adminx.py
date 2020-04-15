import xadmin
from xadmin import views

from django.contrib.auth.models import Group, Permission
from xadmin.models import Log

from .models import UserProfile


class BaseSetting(object):
    enable_themes = True  #主题开启
    use_bootswatch = True  #主题开启


class GlobalSettings(object):
    site_title = "Vinson模板管理系统"  #页面左上角
    site_footer = "2020 Vinson模板管理系统"
    # menu_style = "accordion"

    def get_site_menu(self):
        return (
            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
            )},
            {'title': '系统管理', 'menus': (
                {'title': '权限分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},
        )


xadmin.site.register(views.CommAdminView, GlobalSettings)