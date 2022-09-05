from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.fields import ReadOnlyField

from User.models import Script, Content
# --------------------------------------------------


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

# --------------------

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)

# --------------------------------------------------

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['script','is_patched']

# --------------------------------------------------

class ContentSerializer(serializers.ModelSerializer):
    script = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'

    def get_script(self, obj):
        sc = Script.objects.get(content=obj).all()
        serializer = ScriptSerializer(sc, many=True)
        return serializer.data


# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------
