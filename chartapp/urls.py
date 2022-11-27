from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^volt-([0-9]{3})$', view=views.add, name = "add"),
]
