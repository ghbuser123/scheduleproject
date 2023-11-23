from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('schedule.urls')), # schedule.urlsへのURLパターン
 
    path('',include('accounts.urls')), # accounts.urlsへのURLパターン

    # パスワードリセットのためのURLパターン
    path('password_reset/',
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    name='password_reset'), # パスワードリセットの申し込みページ

    path('password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
    name='password_reset_done'), # メール送信完了ページ

    path('reset/<uid64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name='password_reset_confirm'), # パスワードリセットページ

    path('reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
    name='password_reset_complete'), # パスワードリセット完了ページ
]