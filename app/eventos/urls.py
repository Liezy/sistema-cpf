from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'servidores', views.ServidorViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'presencas', views.PresencaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("lista/", views.lista_eventos, name="lista_eventos"),
    path('checkin/<int:evento_id>/', views.checkin_evento, name='checkin_evento'),
    path('relatorio/<int:evento_id>/', views.relatorio_presenca, name='relatorio_presenca'),
    path('exportar/<int:evento_id>/', views.exportar_presenca, name='exportar_presenca'),
]