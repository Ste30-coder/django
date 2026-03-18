from django.urls import path
from teacher import views

urlpatterns = [
    path('teach', views.teacher_home, name='teacher_home'),
]