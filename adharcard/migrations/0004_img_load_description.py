# Generated by Django 5.1 on 2024-09-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adharcard", "0003_alter_img_load_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="img_load",
            name="description",
            field=models.CharField(
                blank=True, default="chin tapak dam dam", max_length=255, null=True
            ),
        ),
    ]
