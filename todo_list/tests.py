from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from .models import Tag, Task


TASK_URL = reverse("todo_list:index")
TAG_URL = reverse("todo_list:tag-list")


class ModelTests(TestCase):
    def test_tag_str_return(self):
        tag_name = "test1"
        tag = Tag.objects.create(
            name=tag_name,
        )
        self.assertEqual(tag.name, tag_name)


class DataTasksTests(TestCase):
    def test_get_tasks_data(self):
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)


class CreateTaskTests(TestCase):
    def test_create_task(self):
        self.task = Task.objects.create(
            content="test",
            datetime=datetime.now(),
        )
        response = self.client.get(TASK_URL)

        all_tasks = Task.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["task_list"]), list(all_tasks))


class DataTagsTests(TestCase):
    def test_get_tags_data(self) -> None:
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, 200)


class CreateTagTests(TestCase):
    def test_create_tag(self) -> None:
        self.tag = Tag.objects.create(
            name="test",
        )
        response = self.client.get(TAG_URL)

        all_tags = Tag.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["tag_list"]), list(all_tags))
