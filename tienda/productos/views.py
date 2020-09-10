# -*- coding: utf-8 -*-

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import render
from tienda.models import Product
from . rest import serializers


class ProductViewSet(viewsets.ModelViewSet):
    """"
    API endpoint para mostrar los productos con un token valido
    """
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        """ Devuelve todo los objetos a un usuario autenticado """
        return self.queryset.order_by('name')

    def perform_create(self, serializer):
        """ Crea un nuevo producto """
        serializer.save(user=self.request.user)


def vista_productos(request):
    if request.session['token']:
        return render(request, 'tienda/productos.html', {})
    return render(request, 'tienda/login.html', {})
