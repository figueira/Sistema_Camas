from simple_history.admin import SimpleHistoryAdmin
from models import *
from django.contrib import admin

# Register your models here.
#admin.site.register(Habitacion)
admin.site.register(Ingreso)

admin.site.register(Habitacion, SimpleHistoryAdmin)