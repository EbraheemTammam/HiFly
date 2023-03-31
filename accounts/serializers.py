from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email', 
            'first_name', 
            'last_name',
            'is_staff',
            'is_college_head',
        )
        read_only_fields = ('is_staff',)

class TokenSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = '__all__'