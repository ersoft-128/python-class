from django.contrib import admin
from django.urls import path

from app.views import about, homepage

urlpatterns = [
    path("",homepage,name='home'),
    path("about/",about,name='about')
]