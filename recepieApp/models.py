from django.db import models

# Create your models here.
class Recepie(models.Model):
    recepieName=models.CharField(max_length=100)
    recepieDescription=models.TextField()
    recepieImage=models.TextField()
    