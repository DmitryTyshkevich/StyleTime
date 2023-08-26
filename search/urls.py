from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.search, name='search'),
    path('<str:text>/', views.filtered_search, name='filtered_search'),
]