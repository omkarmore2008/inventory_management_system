from rest_framework import serializers

from inventory_management_system.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "name"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
