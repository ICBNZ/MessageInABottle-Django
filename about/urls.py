from django.urls import path
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import about, game, team, something_fishy, privacy

# path: url, views file.profile function
urlpatterns = [
    path('about/', views.about, name='about'),
    path('game/', views.game, name='game'),
    path('team/', views.team, name='team'),
    path('privacy/', views.privacy, name='privacy'),
    path('something_fishy/', views.something_fishy, name="something_fishy")
]
