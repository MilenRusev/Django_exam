from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    username = UserModel

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'phone']
        data = {f: validated_data.get(f) for f in fields}
        user = UserModel(**data)
        user.set_password(validated_data['password'])
        user.save()
        return user

