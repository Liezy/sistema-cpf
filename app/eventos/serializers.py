from rest_framework import serializers
from .models import ServidorModel, EventoModel, PresencaModel

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServidorModel
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoModel
        fields = '__all__'

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresencaModel
        fields = '__all__'