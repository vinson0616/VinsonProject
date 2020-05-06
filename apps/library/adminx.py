import xadmin
from .models import LibraryCategory, LibraryMedia


class LibraryCategoryAdmin(object):
    list_display = ['name','parent_category', 'add_time']
    search_fields = ['name','parent_category', 'desc']
    list_filter = ['name','parent_category', 'desc', 'add_time']
    readonly_fields = ['add_time']


class LibraryMediaAdmin(object):
    list_display = ['name','category','has_display','price','discount','click_nums', 'add_time']
    search_fields = ['name','category','has_display','price','discount','click_nums', 'add_time']
    list_filter =  ['name','category','has_display','price','discount','click_nums', 'add_time']
    readonly_fields = ['add_time','click_nums']
    list_editable = ['has_display'] # 列表项是否需要单独编辑


xadmin.site.register(LibraryCategory, LibraryCategoryAdmin)
xadmin.site.register(LibraryMedia, LibraryMediaAdmin)