# Generated by Django 4.2.4 on 2023-08-17 20:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_project_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="body",
            field=ckeditor.fields.RichTextField(max_length=10000),
        ),
    ]
