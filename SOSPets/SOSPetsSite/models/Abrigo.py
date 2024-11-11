from SOSPetsSite.models import *


class Abrigo(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=200)
    capacidade = models.IntegerField()


    def __str__(self):
        return f'{self.nome} - {self.responsavel}'

    class Meta:
        verbose_name = 'Abrigo'
        verbose_name_plural = 'Abrigos'