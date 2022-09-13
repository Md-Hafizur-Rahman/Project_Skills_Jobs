# Generated by Django 4.1 on 2022-09-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_product_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="product",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="is_stock",
            field=models.BooleanField(default=True),
        ),
    ]
