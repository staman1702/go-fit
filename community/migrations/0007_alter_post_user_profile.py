# Generated by Django 3.2.24 on 2024-05-04 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('community', '0006_alter_post_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='posts', to='profiles.userprofile'),
        ),
    ]
