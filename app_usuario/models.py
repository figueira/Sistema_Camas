from django.db import models
from django.contrib.auth.models import User

USUARIO = (
    ('A','Administracion'),
    ('R','Responsable'),
    ('M','Medico'),
    ('L','Limpieza'),
    ('S','Solicitante'),
)

# Create your models here.
class Usuario(User):
    tipo = models.CharField(max_length = 1, choices = USUARIO)

    def is_admin(self):
        return (self.tipo == 'A')

    def is_medico(self):
        return (self.tipo == 'M')

    def is_limpieza(self):
        return (self.tipo == 'L')

    def is_sol(self):
        return (self.tipo == 'S')

    def is_resp(self):
        return (self.tipo == 'R')


    def tipoR(self):
        tipoUsuario = ""
        if self.is_admin():
            tipoUsuario = 'Administracion'

        elif self.is_resp():
            tipoUsuario = 'Responsable'

        elif self.is_medico():
            tipoUsuario = 'Medico'

        elif self.is_limpieza():
            tipoUsuario = 'Limpieza'

        elif self.is_sol():
            tipoUsuario = 'Solicitante'

        return tipoUsuario


    

class Medico(Usuario):
    codigo = models.IntegerField(max_length=3)
    
    def codigo_str(self):
        return str(self.codigo).zfill(3)
    
    def __unicode__(self):
        return "%s, %s (%s)" % (self.last_name, self.first_name, 
                                str(self.codigo).zfill(3))
        
    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
        
