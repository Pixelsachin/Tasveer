from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import os
from django.contrib.auth.models import User

# Create your models here.


def filename(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("only jpg file can be uploded")


class img_load(models.Model):
    image = models.ImageField(upload_to="images/", validators=[filename])
    description = models.TextField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class userprofile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    avatar = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True, validators=[filename]
    )

    bio = models.CharField(max_length=10, default="Friend")

    def save(self, *args, **kwargs):
        if self.pk:
            # Fetch the existing instance
            old_instance = userprofile.objects.get(pk=self.pk)
            # Check if the profile photo has been changed
            if old_instance.avatar and old_instance.avatar != self.avatar:
                # Delete the old photo
                if os.path.isfile(old_instance.avatar.path):
                    os.remove(old_instance.avatar.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
