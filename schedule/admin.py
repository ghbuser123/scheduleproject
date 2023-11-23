from django.contrib import admin
from .models import Category,SchedulePost

# 管理ページのレコード一覧にカラムを設定

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class SchedulePostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')    

# 管理サイトに登録する

admin.site.register(Category,CategoryAdmin)

admin.site.register(SchedulePost,SchedulePostAdmin)