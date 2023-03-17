from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from todo_list.forms import TaskUpdateForm, TaskCreateForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class UpdateStatusView(generic.View):
    model = Task

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_list:index"))


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
