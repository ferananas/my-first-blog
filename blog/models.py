from django.db import models
from django.utils import timezone


class Posst (models.Model):
    schrijver=models.ForeignKey('auth.User')
    titel = models.CharField(max_length=200)
    tekst = models.TextField()
    creatie_datum = models.DateTimeField(default=timezone.now)
    publicatie_datum = models.DateTimeField(blank= True, null=True)

    def publicatie(self):
        self.publicatie_datum=timezone.now()
        self.save()

    def __str__(self):
        return self.titel

# Create your models here.
