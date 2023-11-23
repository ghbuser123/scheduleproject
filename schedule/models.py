from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# 新規イベントのカテゴリーを管理するモデル
class Category(models.Model):
     title = models.CharField(
          verbose_name = 'カテゴリー', 
          max_length = 20,
     )

     def __str__(self):
          return self.title

# 新規イベントの内容を管理するモデル
class SchedulePost(models.Model):
     user = models.ForeignKey(
          CustomUser,
          verbose_name = 'ユーザー',
          on_delete = models.CASCADE, # ユーザー削除でイベントデータも全て削除する
     )

     category = models.ForeignKey(
          Category,
          verbose_name = 'カテゴリー',
          on_delete = models.PROTECT, # カテゴリーにデータがある場合はカテゴリーを削除できない
     )

     title = models.CharField(
          verbose_name = 'タイトル',
          max_length = 20,
     )

     start_date = models.DateField(
          verbose_name = '開始日時', 
          default=timezone.now,
     )
           

     end_date = models.DateField(
          verbose_name = '終了日時',
          default=timezone.now,
          
     )

     memo = models.TextField(
          verbose_name = 'メモ',
          max_length = 200,
     )

     def __str__(self):
          return self.title