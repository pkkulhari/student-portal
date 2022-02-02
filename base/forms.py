from django import forms
from django.contrib.auth.forms import UserCreationForm

from base.models import Student


class _UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(_UserCreationForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
