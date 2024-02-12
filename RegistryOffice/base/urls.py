from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    # Маршруты 
    path('', views.index, name='index'), # общий маршрут
    
    # Маршруты относящиеся к бракам
    path('marriage_list/', views.marriage_list, name='marriage_list'),
    path('add/', views.add_marriage, name='add_marriage'),
    path('marriage/<int:pk>/', views.marriage_detail, name='marriage_detail'),
    path('marriage/<int:pk>/delete/', views.delete_marriage, name='delete_marriage'),
    path('marriage/<int:pk>/edit/', views.edit_marriage, name='edit_marriage'),

    # Маршоуты относящиеся кразводам
    path('divorce_list/', views.divorce_list, name='divorce_list'),
]
