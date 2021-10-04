from django.shortcuts import render
from .models import employes
from .serializers import EmployesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.


class EmployeAPIVIEW(APIView):
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        employe = employes.objects.all()
        serializer = EmployesSerializer(employe, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployesSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
