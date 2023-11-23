from django.contrib import admin
from .models import CustomUser


# 管理ページのレコード一覧に表示するカラムを設定
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username')

    list_display_links = ('id','username')

# 管理サイトに登録
admin.site.register(CustomUser,CustomUserAdmin)    