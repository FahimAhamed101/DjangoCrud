# Generated by Django 5.1 on 2024-10-05 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_tasks_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedfile',
            old_name='feed',
            new_name='tasks',
        ),
    ]
