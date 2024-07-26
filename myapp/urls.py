from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('course', views.course,name='course'),
    path('coursedb', views.coursedb,name='coursedb'),
    path('register', views.register,name='register'),
    path('registerdb', views.registerdb,name='registerdb'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('teacher', views.teacher,name='teacher'),
    path('teachers', views.teachers,name='teachers'),
    path('students', views.students,name='students'),
    path('student_list', views.student_list,name='student_list'),
    path('stud_edit/<int:id>', views.stud_edit,name='stud_edit'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('stud_delete/<int:id>', views.stud_delete,name='stud_delete'),
]