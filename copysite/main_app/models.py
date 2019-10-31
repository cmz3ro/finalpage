from django.db import models
# Create your models here.

class Treni_led(models.Model):
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.image.url

class Treni_rapishot(models.Model):
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.image.url

class Treni_dorojka(models.Model):
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.image.url

class Treni_ofp(models.Model):
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.image.url


