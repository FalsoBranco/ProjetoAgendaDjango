from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField("nome categoria", max_length=50)

    def __str__(self) -> str:
        return self.nome


class Contato(models.Model):
    nome = models.CharField("nome contato", max_length=255)
    sobrenome = models.CharField("sobrenome contato", max_length=255, blank=True)
    telefone = models.CharField("telefone contato", max_length=13)
    email = models.CharField("email contato", max_length=254, blank=True)
    data_criacao = models.DateTimeField(
        "data criacao contato",
        auto_now=True,
    )
    descricao = models.TextField("descricao contato", blank=True)
    categoria = models.ForeignKey(
        "contatos.Categoria",
        verbose_name="categoria contato",
        on_delete=models.DO_NOTHING,
    )
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d")

    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contatos"

    def __str__(self):
        return self.nome
