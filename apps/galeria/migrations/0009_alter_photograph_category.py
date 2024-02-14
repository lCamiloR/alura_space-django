# Generated by Django 5.0.1 on 2024-02-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0008_alter_photograph_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photograph",
            name="category",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("ESTRELA", "Estrela"),
                    ("GALAXIA", "Galaxia"),
                    ("PLANETA", "Planeta"),
                    ("LUA", "Lua"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
