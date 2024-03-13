from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): #Heredando tabla de usuario de Django
    nombre = models.CharField(max_length=255)

class Profile(models.Model): #Clase Perfil con relacion a un usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    foto = models.ImageField(upload_to='Perfiles', blank=True, null=True)

    def __str__(self):
        return self.user.nombre
    