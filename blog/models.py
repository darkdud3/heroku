from statistics import mode
from django.db import models
from django.contrib.auth.models import User
#da pra aperta ctrl+click no 'User' pra ver a documentacao
from django.urls import reverse

# Create your models here.


class Post(models.Model):
#post é a classe, vamos criar uma tabela para armazenar os posts

    title = models.CharField(max_length=255)
    #encontra tudo na documentação, tipo se pode vazio ou nao, se vem algum valor padrao ou nao etc
    #titulo do post
    
    slug = models.SlugField(max_length=255, unique=True)
    #slug é o nome que vai ser dado a postagem no url
    #ex se o slug for introducao-ao-django, seria wwww.meusite.com\blog\introducao-ao-django

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #aqui ta pegando o ID do usuário pra ver quem foi o autor do post
    #caso o usuario for deletado, o cascade faz com que o post seja deletado tb

    body = models.TextField()
    #corpo do post, nao precisa de max_lenght que nem o titulo

    created = models.DateTimeField(auto_now_add=True)
    #adiciona automaticamente a data e hora quando o post for criado

    updated = models.DateTimeField(auto_now=True)
    #quando atualizar o post, vai pegar a data e hora da ultima atualizacao

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})