from django import forms
from .models import img_load


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = img_load
        fields = ("image",)
