import json

from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt import settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        user = {
            "pk": self.user.pk,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "phone": str(self.user.phone),
            "role": self.user.role
        }
        data["user"] = json.dumps(user)
        if settings.api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
