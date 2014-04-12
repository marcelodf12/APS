from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    """Este es el modelo 'Usuario' con sus atributos, al sincronizar con la Base de Datos la clase se convertira
    en una tabla y sus atributos se traduciran en campos de la misma."""

    user = models.OneToOneField(User)           # Clave foranea a la tabla users del administrador de django
    estado = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)

    def __unicode__(self):
        """ Metodo llamado para visualizar objetos. En este caso se utilizara la clave foranea 'user'
        para acceder al campo 'username' cuyo contenido se mostrara como referencia a cada instancia del
        modelo Proyectos  """
        return self.user.username