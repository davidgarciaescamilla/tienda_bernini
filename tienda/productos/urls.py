from django.urls import path
from . import Ajax, views

urlpatterns = [

    path('', views.vista_productos, name='vista_productos'),

    path('login/', Ajax.login, name='login'),
    path('get_products/', Ajax.get_products, name='get_products'),
]
