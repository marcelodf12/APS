from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User)
    estado = models.TextField()
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.TextField()

    def __unicode__(self):
        return self.user.username
