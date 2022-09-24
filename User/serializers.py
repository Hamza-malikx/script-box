from rest_framework import serializers
# from django.contrib.auth.models import get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.fields import ReadOnlyField

from User.models import *


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

class ContentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


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

class BadgeContentSerializer(serializers.ModelSerializer):
    content = ReadOnlyField(source='content.id')
    # content_id = serializers.ReadOnlyField(source='content.title')
    badge = serializers.SerializerMethodField(read_only=True)
    # content = ContentIDSerializer(many=False, read_only=True)
    # content = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BadgeContent
        fields = ['badge','content']

    def get_badge(self, obj):
        bg = Badge.objects.get(name=obj.badge.name)
        serializer = BadgeSerializer(bg, many=False)
        return serializer.data

    def get_content(self, obj):
        con = Content.objects.get(id=obj)
        serializer = ContentIDSerializer(con, many=False)
        return serializer.data

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'



# --------------------------------------------------

class CommentSerializer(serializers.ModelSerializer):
    content = ReadOnlyField(source='content.title')
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'

class FavSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField(read_only=True)
    user = ReadOnlyField(source='user.username')

    class Meta:
        model = FavContent
        fields = '__all__'

    def get_content(self, obj):
        con = Content.objects.get(title=obj.content.title)
        serializer = ContentIDSerializer(con, many=False)
        return serializer.data

# --------------------------------------------------

# --------------------------------------------------
