# Generated by Django 4.2.20 on 2025-03-18 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_services_images1_services_images10_services_images2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='image',
            new_name='head_image',
        ),
    ]
