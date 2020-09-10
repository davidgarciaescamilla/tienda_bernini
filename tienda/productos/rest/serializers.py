# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from rest_framework import serializers
from tienda.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serialize a product"""
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'amount'
        )
        read_only_fields = ('id',)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer para el objeto de autenticación"""
    name = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
        )

    def validate(self, attrs):
        """valida y autentica al usuario"""
        name = attrs.get('name')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=name,
            password=password
        )

        if not user:
            msg = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
