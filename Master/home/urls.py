from django.contrib import admin
from django.urls import path, include, re_path
from home import views
urlpatterns = [
    path('get_colleges', views.get_colleges, name="get_colleges"),
    path('by_name/<str:name>', views.by_name, name="by_name"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),


]
