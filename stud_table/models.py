from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phoneno=models.IntegerField()
    
    