# Generated by Django 5.0.1 on 2024-02-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0007_photograph_photograph_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photograph",
            name="published",
            field=models.BooleanField(default=True),
        ),
    ]
