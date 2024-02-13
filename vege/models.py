from django.db import models
from django.contrib.auth.models import User #yee django ka pre-built model hota h 



# Create your models here.

class Receipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    receipe_name=models.CharField(max_length=100)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="receipe")