# Generated by Django 5.1.7 on 2025-04-15 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_plant_next_owner_transfers'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='light_requirements',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='species',
            name='soil_type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='species',
            name='temperature_range',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='species',
            name='watering_frequency',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='plant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='transfer', to='app.plant'),
        ),
    ]
