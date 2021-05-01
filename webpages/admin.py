from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):       # it is created to unlock some inbuilt feature for admin panel.

    def myphoto(self,object):
        return format_html("<img src = '{}' width = '40' class='img-circle' alt='Cinque Terre' />".format(object.photo.url))
    
    list_display = ('id','myphoto','first_name','role','created_date')           # to display names on Team table in admin panel.
    list_display_links = ('first_name','id',)                # which field want to work as an link .
    list_filter = ('role',)                       # just to filter the table based on fields in tables.
    search_fields = ('first_name','last_name',)    # eanbles search bar into admin panel.





admin.site.register(Slider)
admin.site.register(Team ,TeamAdmin)