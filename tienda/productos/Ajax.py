# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from tienda.models import Product

import json


 # método con el que nos logueamos y obtenemos el id del usuario si las credenciales son correctas
def login(request):
    if request.is_ajax():
        form = request.POST
        username = form.get('user')
        password = form.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if not user:
            request.session['token'] = False
            msg = 'Unable to authenticate with provided credentials'
        else:
            me = User.objects.get(username=username)
            request.session['token'] = me.id
            msg = 'User authenticated'
    return HttpResponse(json.dumps(msg),
                        content_type="application/json")


# método para crear productos
def product_create(request):
    msg = False
    if request.is_ajax():
        form = request.POST
        try:
            id = request.session['token']
            Product.objects.create(user_id=id, title=form.get('name'),
                                   price=form.get('price'),
                                   amount=form.get('amount'))
            msg = 'Product has been created'
        except Exception as e:
            msg = str(e)
            print(str(e))
        return HttpResponse(json.dumps(msg),
                            content_type="application/json")


# método ajax para rellenar la tabla de los productos automáticamente
def get_products(request):
    d_result = {
        'data': []
    }
    if request.is_ajax():
        products = Product.objects.all()
        l_products = list(products.values("pk", "title", "price"))
        for value in l_products:
            valores = {
                'pk': value['pk'],
                'name': value['title'],
                'price': str(value['price']),
            }
            d_result['data'].append(valores)
    return HttpResponse(json.dumps(d_result), content_type="application/json")
