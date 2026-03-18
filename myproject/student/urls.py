from django.urls import path

from student import views


urlpatterns = [
    path('home/', views.myhome),
    path('edit_profile/',views.edit_profile, name='edit_profile'),

]
