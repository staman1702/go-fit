# Generated by Django 3.2.24 on 2024-05-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='product_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]