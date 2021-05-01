from django.contrib import admin
from .models import Hiretuber
from django.utils.html import format_html
# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):


    list_display = ('user_id','first_name','tuber_name','city','mobile','created_date',)
    list_display_links = ('user_id','first_name',)
    search_fields = ('first_name','city','tuber_name',)
    list_filter = ('city','state',)

admin.site.register(Hiretuber,HiretuberAdmin)