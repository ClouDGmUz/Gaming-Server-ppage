from django.urls import path
from . import views

app_name = 'discord_server'

urlpatterns = [
    path('', views.home, name='home'),
]