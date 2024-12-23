from django.contrib import admin
from.models import Page, PostFileContent

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','user',]
    list_display_links = ['id','title','content','user',]


@admin.register(PostFileContent)
class PostFileContentAdmin(admin.ModelAdmin):
    list_display = ['id','user','posted']
    list_display_links = ['id','user','posted']
    