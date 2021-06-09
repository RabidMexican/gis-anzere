from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('parking/all', views.all_parking),
    path('gare/all', views.all_gare),
    path('commerce/all', views.all_commerce),
    path('passage/all', views.all_passage),
    path('piste/all', views.all_piste),
    path('telecabine/all', views.all_telecabine),
    path('telesiege/all', views.all_telesiege),
    path('teleski/all', views.all_teleski),
]
