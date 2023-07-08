from django.urls import path
from . import views

app_name = 'guarantee_returns'
urlpatterns = [
    path('', views.guarantee_returns, name='guarantee_returns'),

]