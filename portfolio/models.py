from django.db import models

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='portfolio/images')



    def __str__(self):
        return self.title

class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 100)
    message = models.TextField(max_length = 1000)

    def __str__(self):
        return self.email