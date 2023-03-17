from django import forms

from .models import Tag, Task
from django.forms.widgets import NumberInput


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    deadline = forms.DateTimeField(
        label="Date",
        required=True,
        widget=NumberInput(attrs={"type": "date"})
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TaskUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    deadline = forms.DateTimeField(
        label="Date",
        required=True,
        widget=NumberInput(attrs={"type": "date"})
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
