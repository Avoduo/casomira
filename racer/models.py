from django.db import models
from django import forms

class Zavod(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=12)
    info = models.CharField(max_length=3000, default='')

    def __str__(self):
        return self.name +', ' +  self.date

class Racer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    CHOICES_sex = [
        ('M', 'muž'),
        ('F', 'žena'),
    ]
    sex = models.CharField(max_length=10, choices=CHOICES_sex, null=True)

    phone = models.IntegerField(null=True)
    date = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, default='')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    
