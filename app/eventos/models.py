from django.db import models

class Servidor(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255)
    setor = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Presenca(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    sincronizado = models.BooleanField(default=False) # Indica se foi sincronizado com o servidor

    class Meta:
        unique_together = ('servidor', 'evento')

    def __str__(self):
        return f"{self.servidor.nome} - {self.evento.nome}"