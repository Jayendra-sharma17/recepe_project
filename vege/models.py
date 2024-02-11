from django.db import models

# Create your models here.

class Receipe(models.Model):
    Receipe_name=models.CharField(max_length=100)
    Receipe_description=models.TextField()
    Receipe_image=models.ImageField(upload_to="receipe")