from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import SignUpView, profile, edit_profile, edit_password, add_address
#PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
	path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_password/', views.edit_password, name='edit_password'),
    path('add_address/', views.add_address, name='add_address'),
    path('', views.home_blogs, name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_form_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='reset_complete'),
]
