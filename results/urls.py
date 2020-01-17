from django.contrib import admin
from django.urls import path
from .views import view_studs, enter_stud

urlpatterns = [
    path('', view_studs, name='view_studs'),
    path('enter_stud/', enter_stud, name='enter_stud'),
]
