from django.db import models
from sanitizer.models import SanitizedCharField, SanitizedTextField
# Create your models here.
class Product(models.Model): #new
    name = models.CharField("Name", max_length=240)
    name = SanitizedCharField(max_length=240, allowed_tags=["a","p","input"])
    description = models.TextField(default="Some description")
    description = SanitizedTextField(allowed_tags=["a","p","input"])
    id = models.UUIDField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    image = models.URLField(default="https://jsonplaceholder.typicode.com/")
    image = SanitizedTextField(allowed_tags=["a","p","input"])
    category = models.CharField(default="Some Category", max_length=240)
    category = SanitizedCharField(allowed_tags=["a","p","input"],max_length=240)

    def __str__(self):
        return self.name