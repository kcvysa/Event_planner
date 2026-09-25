from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_event, name='add_event'),
    path('settings/', views.settings_view, name='settings'),
    path('about/', views.about, name='about'),
]