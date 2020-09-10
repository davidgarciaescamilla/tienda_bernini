from django.shortcuts import render
from tienda.models import Product

from django.http import JsonResponse


def vista_productos(request):
    if request.session['token']:
        return render(request, 'tienda/productos.html', {})
    return render(request, 'tienda/login.html', {})


def lista_productos(request):
    if not request.session['token']:
        return render(request, 'tienda/login.html', {})
    MAX_OBJECTS = 20
    products = Product.objects.all()[:MAX_OBJECTS]
    data = {"results": list(products.values("pk", "title", "price"))}
    return JsonResponse(data)
