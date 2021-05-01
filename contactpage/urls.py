from django.urls import path 

from . import views

urlpatterns = [
    path('',views.reachus, name='reachus'),
]
