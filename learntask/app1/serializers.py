from rest_framework import serializers
from . models import Users,Teams


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields= '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teams
        fields = '__all__'


