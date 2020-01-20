from django.db import models

# Create your models here.
class USERS(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    is_staff = models.CharField(max_length=5)

class PROJECTION(models.Model):
    name = models.CharField(max_length=30)
    time = models.DateField()
    place = models.CharField(max_length=30)

class TICKET(models.Model):
    buyer = models.ForeignKey(USERS, on_delete=models.CASCADE)
    projection = models.ForeignKey(PROJECTION, on_delete=models.CASCADE)
