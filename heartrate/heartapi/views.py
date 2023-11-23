from django.shortcuts import render
from rest_framework import serializers, viewsets
from heartapi.serializer import BatimentosSerializer
from heartapi.models import Batimentos

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Create your views here.


class BatimentosViewSet(viewsets.ModelViewSet):
    queryset = Batimentos.objects.all()
    serializer_class = BatimentosSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    search_fields = ['id_paciente']
