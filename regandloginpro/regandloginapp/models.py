from django.db import models

class RegistrationData(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=20)
    date_of_birth=models.DateField(max_length=50)
    def __str__(self):
        return self.username
