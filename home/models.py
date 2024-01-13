from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='Home/%Y/%m/%d')
    