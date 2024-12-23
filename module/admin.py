from django.contrib import admin
from.models import Module

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id','title','user','hours',]
    list_display_links = ['id','title','user','hours',]
