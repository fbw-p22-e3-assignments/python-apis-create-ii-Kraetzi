from django.db import models

# Create your models here.
class Product(models.Model): #new
    name = models.CharField("Name", max_length=240)
    description = models.TextField(default="Some description")
    id = models.UUIDField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    image = models.URLField(default="https://jsonplaceholder.typicode.com/")
    category = models.CharField(default="Some Category", max_length=240)

    def __str__(self):
        return self.name