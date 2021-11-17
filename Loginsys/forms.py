from django import forms
from django.forms import fields
from Loginsys.models import editUpdateRecord


class recforms(forms.ModelForm):
    class Meta:
        model = editUpdateRecord
        fields = "__all__"
