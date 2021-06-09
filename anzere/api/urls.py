from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('parking/all', views.all_parking),
    path('gare/all', views.all_gare),
]
