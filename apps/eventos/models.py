from django.db import models
from apps.membros.models import Membros
from datetime import date


class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nome_evento = models.CharField(max_length=100)
    responsavel = models.ForeignKey(
        Membros,
        on_delete=models.CASCADE,
        related_name="evento_responsavel",
    )
    data_evento = models.DateField()

    def __str__(self):
        return self.nome_evento


class InscricaoEvento(models.Model):
    id = models.AutoField(primary_key=True)
    membro_participante = models.ForeignKey(
        Membros,
        on_delete=models.CASCADE,
        related_name="eventos_participante",
    )
    data_inscricao = models.DateField(default=date.today)

    def __str__(self):
        return f"Cadastro ID: {self.id}, Membro: {self.membro_participante.nome_completo}"
