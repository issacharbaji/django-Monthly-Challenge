from django.urls import path
from . import views

urlpatterns = [
    path('<str:challenge>/', views.index),
]
