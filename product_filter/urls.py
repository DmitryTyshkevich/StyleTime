from django.urls import path
from . import views

app_name = 'product_filter'
urlpatterns = [
    path('', views.product_filter, name='product_filter'),

]