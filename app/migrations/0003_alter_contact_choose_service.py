# Generated by Django 4.2.20 on 2025-03-17 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact_choose_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='choose_service',
            field=models.ForeignKey(blank=True, default='Vehicle Body Building', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.services'),
        ),
    ]
