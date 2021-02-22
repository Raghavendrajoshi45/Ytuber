from django.contrib import admin

from .models import  Slider , Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))



    list_display = ('id','myphoto', 'first_name' , 'created_date', )
    list_display_links=('first_name', 'id',)
    search_fields=('first_name', 'created_date',)
    list_filter=('first_name'),

# Register your models here.
admin.site.register(Slider)

admin.site.register(Team, TeamAdmin)