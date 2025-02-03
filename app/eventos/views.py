from django.http import HttpResponse
from rest_framework import viewsets
from .models import Servidor, Evento, Presenca
from .serializers import ServidorSerializer, EventoSerializer, PresencaSerializer

def home(request):
    return HttpResponse("Bem-vindo à API de Eventos")

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer