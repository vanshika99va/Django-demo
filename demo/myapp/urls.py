from django.contrib import admin
from django.urls import path
from . import views

urlpatterns= [
    path("",views.home, name="home"),
    path("todos/",views.todos, name="Todos"),
    path('admin/', admin.site.urls)
    ]