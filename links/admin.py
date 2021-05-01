from django.contrib import admin
from .models import Links



# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id','email','twitter','fb_link','mobile',)
    list_display_links = ('id','email',)

admin.site.register(Links,LinksAdmin)