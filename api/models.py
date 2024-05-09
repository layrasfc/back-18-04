from django.db import models

import uuid  # id do usuario logado

def upload_image(instance, file_name):
    # nome do arquivo vai ser o código do user + nome da foto
    return f"{file_name}" 

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)

    # aceitar nenhuma imagem (blank) e cancelar uma imagem (null)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
