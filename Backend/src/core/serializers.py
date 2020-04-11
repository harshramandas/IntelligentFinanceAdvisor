from rest_framework import serializers

from .models import UserData, User

class UserDataSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = (
            'name', 'amount', 'cashflow', 'category', 'interval', 'description'
        )

class UserDataSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = (
            'name', 'amount', 'cashflow', 'category', 'interval', 'description', 'id'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'