# Generated by Django 3.2.24 on 2024-05-04 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user_profile',
        ),
    ]