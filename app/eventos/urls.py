from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'servidores', views.ServidorViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'presencas', views.PresencaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]