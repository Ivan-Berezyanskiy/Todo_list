from django import forms

from .models import Tag, Task


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TaskUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
