from django.db import models

# Create your models here.
class Contact_page(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=50)
    message = models.TextField()
