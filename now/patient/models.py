from django.db import models
from datetime import datetime, date, time
from django.utils import timezone
from django.contrib.auth import authenticate, login, get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
# Create your models here.
User = get_user_model()

class PatientProfileManager(models.Manager):
    def  create_user(self, profile, name, email , age, address, birth_date, gender, contact_number):
        if not name:
            raise ValueError("Profile should have a name")
        if not email:
            raise ValueError("Profile should have an email")
        if not age:
            raise ValueError("Profile should have an age")
        if not address:
            raise ValueError("Profile should have a primary address")
        if not birth_date:
            raise ValueError("Profile should have a birthdate")
        if not gender:
            raise ValueError("Profile should have a gender")
        if not contact_number:
            raise ValueError("Profile should have a primary contact number")
        user = self.model(
            name = name,
            email = email,
            age = age,
            address = address,
            birth_date = birthdate,
            gender = gender,
            contact_number = contact_number,
        )
        return user, profile

class PatientProfile(models.Model):
    GENDER_CHECK = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    profile = models.OneToOneField(User, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(max_length=255, null=True, blank=False, unique=True)
    address = models.CharField(max_length=255, null=True)
    age =  models.PositiveIntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=False, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHECK)
    contact_number = models.CharField(max_length=11, blank=False, null=True)


    objects = PatientProfileManager()

    def __str__(self):
        return self.name
