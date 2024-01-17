from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers


class LoginSerializer(RestAuthLoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
