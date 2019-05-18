from django.db import models


# this is from server side code

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')
    doc = models.FileField(upload_to='Doc/' , default='Doc/None/No-docs.PDF')
