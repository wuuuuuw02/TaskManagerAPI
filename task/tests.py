from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.other_owner = User.objects.create_user(
            username="other_owner", password="pass"
        )
        self.test_user = User.objects.create_user(username="test1", password="UDRA6WVl")
        self.task1 = Task.objects.create(
            title="Новая задача 1",
            description="asd",
            status="in_progress",
            owner=self.other_owner,
        )
        self.task2 = Task.objects.create(
            title="Новая задача 2",
            description="asd",
            status="in_progress",
            owner=self.test_user,
        )

    def test_anonymous_cannot_access_tasks(self):
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_sees_only_own_tasks(self):
        self.client.force_authenticate(user=self.other_owner)
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    def test_create_task_fails_with_short_title(self):
        self.client.force_authenticate(user=self.other_owner)
        response = self.client.post(
            reverse("task-list"),
            {"title": "Hi", "description": "123", "status": "pending"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_update_other_user_task(self):
        # DRF возвращает 404, если объект не входит в get_queryset()
        self.client.force_authenticate(user=self.other_owner)
        response = self.client.put(
            reverse("task-detail", args=[self.task2.id]),
            {"title": "Попытка изменить", "description": "123", "status": "pending"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
