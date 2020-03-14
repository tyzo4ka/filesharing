from webapp.models import File
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = File
        fields = ('id', 'author', 'file', "caption", 'created_date')
