# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from tienda.models import Product

import json


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


def get_products(request):
    d_result = {
        'data': []
    }
    if request.is_ajax():
        products = Product.objects.all()
        l_products = list(products.values("pk", "title", "price", "amount"))
        for value in l_products:
            valores = {
                'pk': value['pk'],
                'name': value['title'],
                'price': str(value['price']),
                'amount': str(value['amount']),
            }
            d_result['data'].append(valores)
    return HttpResponse(json.dumps(d_result), content_type="application/json")
