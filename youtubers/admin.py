from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YtAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html("<img src = '{}' width = '50' ".format(object.photo.url))


    list_display = ('id','first_name','myphoto','camera_type',"subs_count",'is_featured')
    list_display_links = ('id','first_name',)
    search_fields = ('first_name','city','camera_type',)
    list_filter = ('is_featured','city','camera_type',)
    list_editable = ('is_featured',)      # just to do changes from the table only.


admin.site.register(Youtuber,YtAdmin)
