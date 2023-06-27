from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('<str:producer>/', views.catalogue, name='catalogue'),
    path('<str:producer>/<int:pk>/', views.watch, name='watch'),


]
