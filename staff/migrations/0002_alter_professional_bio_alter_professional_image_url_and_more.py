# Generated by Django 4.2.7 on 2023-11-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_addon'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='professional',
            name='image_url',
            field=models.ImageField(null=True, upload_to='professional'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='subservices',
            field=models.ManyToManyField(related_name='professionals', to='service.subservice'),
        ),
    ]
