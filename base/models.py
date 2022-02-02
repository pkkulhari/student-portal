from django.db import models
from django.contrib.auth.models import User

MARITAL_STATUS_CHOICES = [("MRD", "Married"), ("SGL", "Single")]


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(
        max_length=20, verbose_name="Full Name", null=True, blank=True
    )
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    maritalStatus = models.CharField(
        max_length=10,
        choices=MARITAL_STATUS_CHOICES,
        verbose_name="Marital Status",
        null=True,
        blank=True,
    )
    address = models.TextField(null=True, blank=True)
