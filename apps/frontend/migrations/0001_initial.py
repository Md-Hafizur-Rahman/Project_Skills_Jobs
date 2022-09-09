# Generated by Django 4.1 on 2022-08-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomeSlider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("content", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="slider")),
                ("link", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
