from django.shortcuts import render
from .permissions import IsAdminOrVetOrReadOnly, IsAdminDeleteOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Owner
from .serializers import OwnerSerializer
import logging

logger = logging.getLogger(__name__)

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated, IsAdminOrVetOrReadOnly, IsAdminDeleteOnly]

    def destroy(self, request, *args, **kwargs):
        logger.info(f"Attempting to delete owner. User: {request.user.username}, Role: {request.user.role}")
        logger.info(f"Request method: {request.method}")
        logger.info(f"Authorization header: {request.headers.get('Authorization', 'No Auth header')}")
        return super().destroy(request, *args, **kwargs)

# Create your views here.
