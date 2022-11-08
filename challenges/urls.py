from django.urls import path
from . import views

urlpatterns = [
    path('<str:month>/', views.index,name='month_num'),
    path('<int:num>',views.month_num)
]
