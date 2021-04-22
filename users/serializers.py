from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "full_name")

    def get_full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)



