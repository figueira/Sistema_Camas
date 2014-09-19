from django_cron import CronJobBase, Schedule
from app_camas.models import Habitacion

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app_estadisticas.prueba'    # a unique code

    def do(self):
        hab = Habitacion(
                numero = 777,
                tipo = 'H'
                )
        hab.save()