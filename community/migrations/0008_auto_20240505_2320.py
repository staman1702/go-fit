# Generated by Django 3.2.24 on 2024-05-05 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_post_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
    ]
