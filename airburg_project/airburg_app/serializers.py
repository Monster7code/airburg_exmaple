from .models import *
from rest_framework import serializers


class CapitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitan
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"
