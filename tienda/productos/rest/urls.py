from django.conf.urls import url, include
from rest_framework import routers
from tienda.productos import views
from . import views as rest_views
from django.urls import path

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    url('', include(router.urls)),
    path('token/', rest_views.CreateTokenView.as_view(), name='token'),
]
