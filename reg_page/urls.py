from django.urls import path
from django.shortcuts import redirect
from reg_page.views import *

urlpatterns = [
    path('', lambda request: redirect('home1')),
    path('mainpage/', home1, name='home1'),
    path('studentlist/', studentlist, name='studentlist'),
    path('courselist/', courselist, name='courselist'),
    path('register/', register, name='register'),
    path('enrolledlist/', enrolledStudents, name='enrolledStudents'),
]
