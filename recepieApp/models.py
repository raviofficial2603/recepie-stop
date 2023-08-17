from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recepie(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    recepieName=models.CharField(max_length=100)
    recepieDescription=models.TextField()
    recepieImage=models.TextField()
    