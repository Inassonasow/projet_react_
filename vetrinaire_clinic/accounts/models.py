from django.db import models
from django.contrib.auth.models import AbstractUser

#Créer un modèle utilisateur personnalisé avec rôle
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('vet', 'Vétérinaire'),
        ('reception', 'Réceptionniste'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reception')

# Create your models here.
