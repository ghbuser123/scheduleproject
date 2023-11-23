from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),

    path('entry/',views.CreateScheduleView.as_view(),name='entry'),

    path('entry_done/',views.EntrySuccessView.as_view(),name='entry_done'),

    path('mypage/',views.MypageView.as_view(),name='mypage'),

    path('emailme/',views.EmailmeView.as_view(),name='emailme'),
]