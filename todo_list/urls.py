from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskDeleteView, TaskCreateView, TaskUpdateView
)

urlpatterns = [
                  path(
                      "",
                      TaskListView.as_view(),
                      name="index"
                  ),
                  path(
                      "task/<int:pk>/done-undone/",
                      TaskListView.as_view(),
                      name="done-undone",
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
                  path(
                      "task/<int:pk>/delete",
                      TaskDeleteView.as_view(),
                      name="task-delete"
                  ),
                  path(
                      "task/<int:pk>/update",
                      TaskUpdateView.as_view(),
                      name="task-update"
                  ),
                  path(
                      "task/create",
                      TaskCreateView.as_view(),
                      name="task-create"
                  ),
                  path(
                      "tags/<int:pk>/delete",
                      TagDeleteView.as_view(),
                      name="tag-delete"
                  ),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "todo_list"
