from rest_framework import serializers
# from django.contrib.auth.models import get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.fields import ReadOnlyField

from User.models import Script, Content, NormalUser


# --------------------------------------------------
        
class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'username', 'email']

    # def get_name(self, obj):
    #     name = obj.first_name
    #     if name == '':
    #         name = obj.email

    #     return name


# --------------------

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'username', 'email', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)


# --------------------------------------------------

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['id', 'script', 'is_patched','is_encrypted']


# --------------------------------------------------

class ContentSerializer(serializers.ModelSerializer):
    script = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'

    def get_script(self, obj):
        sc = Script.objects.filter(content=obj)
        serializer = ScriptSerializer(sc, many=True)
        return serializer.data

# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------
