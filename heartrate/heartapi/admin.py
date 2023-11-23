from django.contrib import admin
from heartapi.models import Batimentos
# Register your models here.


class BatimentosAdmin(admin.ModelAdmin):
    fields = ('id_paciente', 'pulsacao', 'datahora')


admin.site.register(Batimentos, BatimentosAdmin)
