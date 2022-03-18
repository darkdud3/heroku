from django.contrib import admin

# Register your models here.
from .models import Post

#para adicionar uma aba de 'posts' na interface de admin 
@admin.register(Post)

#PostAdmin são os campos que quer mostrar na tela
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
