from rest_framework import serializers
from .models import Adoption
from users.serializers import UserSerializer
from pets.serializers import PetSerializer
from rest_framework.exceptions import ValidationError

class AdoptionSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    pet = PetSerializer(read_only=True)

    class Meta:
        model = Adoption
        fields = ("id", "user", "user_id", "pet", "pet_id", "date", "description")
        extra_kwargs = {
            "user_id":{"source":"user", "write_only":True},
            "pet_id":{"source":"pet", "write_only":True},
        }

    def create(self, validated_data):
        if Adoption.objects.filter(pet=validated_data.get("pet")).exists():
            raise ValidationError("Esta mascota, ya ha sido adoptada.")
        adoption = Adoption.objects.create(**validated_data)
        return adoption
