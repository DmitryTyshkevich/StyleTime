from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    # path('', views.index, name='index'),
    path('<str:producer>/', views.catalogue, name='catalogue'),
    path('<str:producer>/<int:pk>/', views.watch, name='watch'),
    # path('shop/', views.shop, name='shop')

]
