from django import forms
from .models import *
from multiupload.fields import MultiFileField, MultiMediaField


class DescriptionForm(forms.Form):
    description = forms.CharField(
        label="Описание", widget=forms.Textarea(attrs={"rows": 5})
    )


class SectionForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["name", "developer", "image_file"]
