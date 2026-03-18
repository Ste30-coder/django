"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_first_app import views
from my_first_app.views import*
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sh/',views.myhome), 
    path('w/<int:age>/',views.welco),
    path('w/<age>',views.welco),    
    path('regE',views.Empreg),
    path('mystat',views.mystatic),
    path('studenthome/',views.myhome),   
    path('listEmp',views.emp_list),
    path('del/<int:gg>/',views.emp_del), 
    path('edit/<int:i>/',views.emp_upd),
    path('update/<int:i>/',views.emp_update),
    path('studreg/',views.stud_reg),
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.logout, name='logout'),
    path('student_list/', views.reg_student_list, name='reg_student_list'),
   
    path('set_session/',views.set_session,name='set_session'),
    path('get_session/',views.get_session,name='get_session'),
    path('delete_session/',delete_session,name='delete_session'),
    path('shhs/',views.shhs,name='shhs'),
    
    path('set_cookie/',set_cookieeee,name='set_cookie'),
    path('get_cookie/',get_cookieeee,name='get_cookie'),
    
    path('upload_file/',upload_file,name='upload_file'),
    path('list_files/',list_files,name='list_files'),

    path('send_eml/',send_eml,name='send_eml'),
    
    path('student/', include('student.urls')), 
    path('teacher/', include ('teacher.urls')),
    
    path('student/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('students/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
    
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


