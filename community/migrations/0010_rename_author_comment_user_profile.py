# Generated by Django 3.2.24 on 2024-05-06 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user_profile',
        ),
    ]