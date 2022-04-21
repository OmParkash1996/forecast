from rest_framework import serializers
from forecast_api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('username'),
                email=validated_data.get('email'),first_name=validated_data.get('first_name'),last_name=validated_data.get('last_name'),password=validated_data.get('password'))
        return  user
