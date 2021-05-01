from django.contrib import admin
from .models import ReachUs
# Register your models here.

class ReachAdmin(admin.ModelAdmin):
    
    list_display = ('id','full_name','email','subject','contact_date',)
    list_display_links = ('id','full_name',)
    search_fields = ('full_name','subject',)
    # list_filter = ('full_name',)

admin.site.register(ReachUs,ReachAdmin)