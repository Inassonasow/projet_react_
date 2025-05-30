from django.db import models


from django.db import models
from owners.models import Owner

class Patient(models.Model):
    TYPE_CHOICES = [
        ('chat', 'Chat'),
        ('chien', 'Chien'),
        ('lapin', 'Lapin'),
    ]

    SEXE_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]
    nom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    type_animal = models.CharField(max_length=10, choices=TYPE_CHOICES)
    race = models.CharField(max_length=100)
    date_naissance = models.DateField()
    poids = models.FloatField()
    proprietaire = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

# Create your models here.
