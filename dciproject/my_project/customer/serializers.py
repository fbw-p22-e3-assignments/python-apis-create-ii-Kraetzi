#new - whole script added by instructor
from rest_framework import serializers 
from .models import Customer
from rest_framework.validators import UniqueTogetherValidator
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['pk', 'name', 'email', 'created']
        validators = [
            UniqueTogetherValidator(
                queryset=Customer.objects.all(),
                fields=["name", "created"],
                message="No Customer Creation in the same year"
            )
        ]
