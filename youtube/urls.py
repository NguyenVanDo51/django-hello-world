from django.urls import path
from . import views

urlpatterns = [
    path('transcript/', views.transcript),
    path('transcript/save', views.save_result, name='save_result')
]