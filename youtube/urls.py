from django.urls import path
from . import views

urlpatterns = [
    path('transcript/', views.transcript),
    path('home/', views.index),
    path('transcript/save', views.save_result, name='save_result')
]