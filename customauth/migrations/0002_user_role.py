# Generated by Django 4.2.7 on 2023-11-14 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('professional', 'Professional'), ('client', 'Client')], default='client', max_length=12),
        ),
    ]
