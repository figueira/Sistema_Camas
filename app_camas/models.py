from django.db import models
from app_solicitudes.models import *
from datetime import date
from simple_history.models import HistoricalRecords

TIPO_HABITACION = (
    ('H','Hospitalizacion'),
    ('A','UCI-A'),
    ('P','UCI-P'),
)

ESTADO_HABITACION = (
    ('D','Disponible'),
    ('O','Ocupada'),
    ('L','En proceso de limpieza'),
    ('A','En proceso de alta'),
    ('M','En mantenimiento'),
)

class Habitacion(models.Model):
    numero    = models.CharField(max_length=6, unique=True)
    reservada = models.BooleanField(default=False)
    estado    = models.CharField(max_length=1, choices=ESTADO_HABITACION, 
                                 default = 'D')
    tipo      = models.CharField(max_length=1, choices=TIPO_HABITACION,
                                 default = 'H')
    razon     = models.CharField(max_length=140, blank = True)
    history   = HistoricalRecords()
    
    def __unicode__(self):
        return "%s" % (self.numero)
        
    def como_termometro(self,fecha):
        return self.history.as_of(fecha)
        
    class Meta:
        verbose_name_plural = "Habitaciones"

    
class Ingreso(models.Model):
    paciente      = models.ForeignKey(Paciente)
    solicitud     = models.ForeignKey(Solicitud)
    habitacion    = models.ForeignKey(Habitacion)
    fecha_ingreso = models.DateField(auto_now_add=True)
    alta          = models.BooleanField(default=False)
    history       = HistoricalRecords()
    
    def procedencia(self):
        return PROCEDENCIA[self.solicitud.procedencia - 1][1]
    
    def num_dias(self):
        today = date.today()
        dias = today - self.fecha_ingreso
        total = dias.days
        if total <= 0:
            total = 1
        return total
    
    def es_hoy(self):
        today = date.today()
        if (today == self.solicitud.fecha_salida):
            return 1
        return 0
        
    def como_termometro1(self,fecha):
        return self.history.as_of(fecha)