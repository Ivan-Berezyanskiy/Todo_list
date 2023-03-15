from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView
)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="index"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
]

app_name = "todo_list"
