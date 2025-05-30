from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from .permissions import IsVetOrReadOnly, IsAdminDeleteOnly
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsVetOrReadOnly, IsAdminDeleteOnly]

# Create your views here.
