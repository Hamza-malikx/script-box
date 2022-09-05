from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from User.models import Script, Content


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    script = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'

    def get_script(self, obj):
        return ScriptSerializer(obj.script, many=False).data
