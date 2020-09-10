from django.urls import path
from . import Ajax, views

urlpatterns = [

    path('', views.vista_productos, name='vista_productos'),
    path('productos/', views.lista_productos, name='lista_productos'),

    path('login/', Ajax.login, name='login'),
    path('product_create/', Ajax.product_create, name='product_create'),
    path('get_products/', Ajax.get_products, name='get_products'),
]
