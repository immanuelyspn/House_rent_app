# Generated by Django 5.1.2 on 2024-11-04 04:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
