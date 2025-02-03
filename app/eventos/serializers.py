from rest_framework import serializers
from .models import Servidor, Evento, Presenca

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'