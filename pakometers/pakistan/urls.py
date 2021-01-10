from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('karachi/',views.karachi,name='karachi'),
    path('islamabad/',views.islamabad,name='islamabad'),
    # path('search/',views.search,name='search'),
    # path('search/',views.search,name='search'),
    path('search/',views.search,name='search'),
]