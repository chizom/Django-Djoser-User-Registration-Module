from django.db.models import fields
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import NewUser

class NewUserSerializer (BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = '__all__'