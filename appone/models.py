from django.db import models

class RegistrationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
