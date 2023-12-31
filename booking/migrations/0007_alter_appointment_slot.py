# Generated by Django 5.0 on 2023-12-22 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_appointment_professional'),
        ('staff', '0005_slot_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='staff.slot'),
        ),
    ]
