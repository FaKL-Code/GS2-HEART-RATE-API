from django.db import models

# Create your models here.


class Batimentos(models.Model):
    id_paciente = models.IntegerField()
    pulsacao = models.IntegerField()
    datahora = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.id_paciente
