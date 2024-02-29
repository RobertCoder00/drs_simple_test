from django.db import models

# Create your models here.
class Project (models.Model):
    title= models.CharField(max_length=200)
    decription = models.TextField()
    tecnologia = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)