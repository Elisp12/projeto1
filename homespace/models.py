from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    index = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    ativo = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    img = models.ImageField(upload_to='media/imagem/%Y/%m/%d/')
    athor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome