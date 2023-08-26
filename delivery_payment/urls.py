from django.urls import path
from . import views

app_name = 'delivery_payment'
urlpatterns = [
    path('', views.delivery_payment, name='delivery_payment'),

]