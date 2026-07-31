from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.none()

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
