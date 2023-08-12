from django.db import models
from apps.membros.models import Membros


class Codigo_Ministerio(models.Model):
    OPCAO_SITUACAO = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    id = models.AutoField(primary_key=True)
    ministerio = models.CharField(max_length=255)
    situacao = models.CharField(max_length=1, choices=OPCAO_SITUACAO, default="")

    def __str__(self):
        return self.nome_do_ministerio_codigo
    

class MembroMinisterio(models.Model):
    OPCAO_SITUACAO = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]

    membro = models.ForeignKey(Membros, on_delete=models.CASCADE)
    data_associacao = models.DateField(auto_now_add=True)
    situacao = models.CharField(max_length=1, choices=OPCAO_SITUACAO, default="A")

    def __str__(self):
        return f"{self.membro} - {self.ministerio} ({self.get_situacao_display()})"
    

class Lideranca_Ministerio(models.Model):
    OPCAO_SITUACAO = [
        ("A", "Ativo"),
        ("I", "Inativo")
    ]
        
    id = models.AutoField(primary_key=True)
    lider = models.ForeignKey(
        to=Membros,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="liderancas",
    )
    ministerio = models.ForeignKey(
        to=Codigo_Ministerio,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="liderancas",
    )
    situacao = models.CharField(max_length=1, choices=OPCAO_SITUACAO, default="")

    def __str__(self):
        return self.id
