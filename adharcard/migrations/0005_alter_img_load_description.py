# Generated by Django 5.1 on 2024-09-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adharcard", "0004_img_load_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="img_load",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
