# Generated by Django 5.1 on 2024-10-05 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_remove_feedfile_images_feedfile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='images',
        ),
    ]
