from datetime import datetime

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(max_length=255, default=datetime.now())
    deadline = models.DateTimeField(max_length=255)
    is_done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-datetime"]
