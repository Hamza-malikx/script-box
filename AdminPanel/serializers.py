from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.fields import ReadOnlyField

from AdminPanel.models import ApplyBadgeCriteria
from User.models import *
# --------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['id', 'script', 'is_patched','is_encrypted']


class ContentSerializer(serializers.ModelSerializer):
    user = ReadOnlyField(source='user.username')
    script = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Content
        fields = '__all__'

    def get_script(self, obj):
        sc = Script.objects.filter(content=obj)
        serializer = ScriptSerializer(sc, many=True)
        return serializer.data


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class BadgeConentSerializer(serializers.ModelSerializer):
    badge = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ApplyBadgeCriteria
        fields = '__all__'

    def get_badge(self, obj):
        bg = Badge.objects.get(id=obj.badge.id)
        print(bg)
        serializer = BadgeSerializer(bg, many=False)
        return serializer.data

# --------------------------------------------------
class StatSerializer(serializers.ModelSerializer):
    Content = serializers.SerializerMethodField(read_only=True)
    # Script = serializers.SerializerMethodField(read_only=True)
    # User = serializers.SerializerMethodField(read_only=True)
    # Badge = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_content(self, obj):
        contents = obj.get_content.all()
        serializer = ContentSerializer(contents, many=True)
        return serializer.data

    # def get_scripts(self, obj):
    #     scripts = Script.objects.all()
    #     serializer = ScriptSerializer(scripts, many=True)
    #     return serializer.data

    # def get_users(self, obj):
    #     content = obj.product_content.all()
    #     serializer = UserSerializer(content, many=True)
    #     return serializer.data

    # def get_badges(self, obj):
    #     reviews = obj.product_review.all()
    #     serializer = BadgeSerializer(reviews, many=True)
    #     return serializer.data

# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------
