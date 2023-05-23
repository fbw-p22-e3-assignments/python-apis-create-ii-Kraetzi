from django.db import models

# Create your models here.

class Customer(models.Model): #new
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
