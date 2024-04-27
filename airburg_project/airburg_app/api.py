from .serializers import *
from rest_framework import viewsets, permissions


class CapitanViewSet(viewsets.ModelViewSet):
    queryset = Capitan.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CapitanSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AirplaneSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer