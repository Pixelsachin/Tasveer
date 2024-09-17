from django import forms
from .models import *


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = img_load
        fields = ("image", "description")


class ProfileForm(forms.ModelForm):

    class Meta:
        model = userprofile
        fields = ["id", "avatar"]
