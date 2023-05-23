from django.db import models
from sanitizer.models import SanitizedCharField, SanitizedTextField
# Create your models here.

class Customer(models.Model): #new
    name = models.CharField("Name", max_length=240)
    name = SanitizedCharField(max_length=240,allowed_tags=["a","p","input"])
    email = models.EmailField(unique=True)
    email = SanitizedTextField(allowed_tags=["a","p","input"])
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    