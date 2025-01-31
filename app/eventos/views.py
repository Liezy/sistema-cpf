from django.http import HttpResponse
from rest_framework import viewsets
from .models import ServidorModel, EventoModel, PresencaModel
from .serializers import ServidorSerializer, EventoSerializer, PresencaSerializer

def home(request):
    return HttpResponse("Bem-vindo à API de Eventos")

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = ServidorModel.objects.all()
    serializer_class = ServidorSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = EventoModel.objects.all()
    serializer_class = EventoSerializer

class PresencaViewSet(viewsets.ModelViewSet):
    queryset = PresencaModel.objects.all()
    serializer_class = PresencaSerializer