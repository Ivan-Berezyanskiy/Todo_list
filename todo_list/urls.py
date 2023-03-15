from django.urls import path

from .views import TaskListView, TagListView

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="index"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list"
    ),
]

app_name = "todo_list"
