from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('record_attn/', views.record_attn, name='record_attn'),
    path('register_user/', views.register_user, name='register_user'),
    path('attn_records/', views.attn_records, name='attn_records'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('register_employee',views.register_employee, name='register_employee'),
    path('gather',views.gather_selfies,name='gather'),
    path('reconize1',views.recognize1,name='recognize1')
]

