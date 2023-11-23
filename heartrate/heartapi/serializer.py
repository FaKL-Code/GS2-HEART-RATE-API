from rest_framework import serializers
from heartapi.models import Batimentos


class BatimentosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batimentos
        fields = ['id_paciente', 'pulsacao', 'datahora']
