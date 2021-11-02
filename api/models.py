from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib import admin
import base64


class Breed(models.Model):
    BREED_SIZES = (
        ('T','Tiny'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=100, blank=False)
    size = models.CharField(max_length=1, choices=BREED_SIZES)
    friendliness = models.IntegerField(blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainiability = models.IntegerField(blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)])
    shedding_amount = models.IntegerField(blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)])
    exercise_needs = models.IntegerField(blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return str(self.name)

class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'size','friendliness','trainiability','shedding_amount','exercise_needs')


class Dog(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False)
    fav_food = models.CharField(max_length=100, blank=False)
    fav_toy = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)

class DogAdmin(admin.ModelAdmin):
    list_display = ('name','age','breed','gender','color','fav_food','fav_toy')

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')
