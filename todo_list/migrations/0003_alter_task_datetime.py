# Generated by Django 4.1 on 2023-03-15 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0002_alter_task_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="datetime",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 15, 17, 41, 24, 15669),
                max_length=255,
            ),
        ),
    ]
