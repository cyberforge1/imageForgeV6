# Generated by Django 4.2.3 on 2023-07-06 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("imageGeneration", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Prompt",
            new_name="Prompts",
        ),
    ]