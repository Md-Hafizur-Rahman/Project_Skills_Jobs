# Generated by Django 4.1 on 2022-09-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_type",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="order",
            name="tnx_id",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
