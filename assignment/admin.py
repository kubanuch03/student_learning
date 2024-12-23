from django.contrib import admin
from .models import Assignment, AssignmentFileContent



@admin.register(AssignmentFileContent)
class AssignmentFileContentAdmin(admin.ModelAdmin):
    list_display = ['id','user']
    list_display_links = ['id','user',]


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','points','due','user']
    list_display_links = ['id','title','content','points','due','user']
