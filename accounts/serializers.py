from dj_rest_auth.serializers import PasswordResetSerializer, LoginSerializer, PasswordResetConfirmSerializer
from rest_framework import serializers
from django.conf import settings

RESET_PASSWORD_REDIRECT_URL = settings.FRONT_END_URLS.get("PASSWORD_RESET") 

def custom_url_generator(request, user, temp_key):
    return f'{RESET_PASSWORD_REDIRECT_URL}/{user.id}/{temp_key}'
class MyLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

class MyPasswordResetSerializer(PasswordResetSerializer):

    def get_email_options(self) :
        return {
            'url_generator': custom_url_generator,
        }
    