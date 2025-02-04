from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Servidor, Evento, Presenca
from .serializers import ServidorSerializer, EventoSerializer, PresencaSerializer
from django.shortcuts import render, get_object_or_404, redirect
import csv

# Views da API
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

# Views dos templates
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/eventos.html', {'eventos': eventos})

def checkin_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        cpf = request.POST.get("cpf")
        servidor = Servidor.objects.filter(cpf=cpf).first()

        if servidor:
            Presenca.objects.create(servidor=servidor, evento=evento)
            return JsonResponse({"status": "success", "message": "Presença registrada!"})
        else:
            return JsonResponse({"status": "error", "message": "CPF não encontrado!"})
        
    return render(request, 'eventos/checkin.html', {'evento': evento})

def relatorio_presenca(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    presencas = Presenca.objects.filter(evento=evento)

    return render(request, 'eventos/relatorio_presenca.html', {
        'evento': evento,
        'presencas': presencas
    })

def exportar_presenca(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    presencas = Presenca.objects.filter(evento=evento)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="presencas_{evento.nome}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Servidor', 'Data e Hora', 'Sincronizado'])

    for presenca in presencas:
        writer.writerow([presenca.servidor.nome, presenca.data_hora, 'Sim' if presenca.sincronizado else 'Não'])

    return response