from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ['owner']

    def validate_title(self, title):
        if not title or len(title) < 5:
            raise serializers.ValidationError("Поле 'title' должно содержать хотя-бы 5 символов.")
        return title.strip()