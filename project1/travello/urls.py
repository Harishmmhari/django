from . import views
from django.urls import path
import  os

urlpatterns = [
    path('index', views.index,name="home"),


]