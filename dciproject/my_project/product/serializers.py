#new - whole script added by instructor
from rest_framework import serializers 
from .models import Product
from rest_framework.validators import UniqueTogetherValidator

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'id', 'created', 'image', 'category']
        validators = [
            UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=["name", "image"],
                message="No identical Products should be added."
            )
        ]
