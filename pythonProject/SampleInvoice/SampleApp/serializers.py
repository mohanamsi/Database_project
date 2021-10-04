

from rest_framework import serializers
from . models import employes


class EmployesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employes
        fields = '__all__'