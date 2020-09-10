# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from tienda.models import Product
from tienda.utils import send_mail

import json


def login(request):
    """ método con el que nos logueamos y obtenemos el id del usuario
    si las credenciales son correctas"""
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


# método ajax para rellenar la tabla de los productos automáticamente
def get_products(request):
    d_result = {
        'data': []
    }
    if request.is_ajax():
        products = Product.objects.all()
        l_products = list(products.values("pk", "name", "price"))
        for value in l_products:
            valores = {
                'pk': value['pk'],
                'name': value['name'],
                'price': str(value['price']),
            }
            d_result['data'].append(valores)
    return HttpResponse(json.dumps(d_result), content_type="application/json")


def send_message(request):
    v_message = {'result': 'not send'}
    if request.is_ajax():
        form = request.POST
        v_message = form.get('message', False)
        v_name = form.get('name', 'anonymous')
        v_email = form.get('email', False)
        if v_email:
            v_message = 'Subject:{}\nFrom: {}\n{}'.format(
                "Cliente Bernini: " + v_name, v_email, v_message)
            send_mail.get_correo(v_email, v_message)
        return HttpResponse(json.dumps(v_message),
                            content_type="application/json")
