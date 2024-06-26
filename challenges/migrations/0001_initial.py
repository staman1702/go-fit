# Generated by Django 3.2.24 on 2024-05-10 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0011_alter_comment_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('main_image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('subjects', models.ManyToManyField(blank=True, to='community.Subject')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='challenge_gallery/')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='challenges.challenge')),
            ],
        ),
    ]
