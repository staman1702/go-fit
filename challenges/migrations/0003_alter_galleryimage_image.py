# Generated by Django 3.2.24 on 2024-05-12 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_challenge_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='challenge_gallery/'),
        ),
    ]