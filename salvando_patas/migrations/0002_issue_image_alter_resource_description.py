# Generated by Django 5.1.4 on 2025-01-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salvando_patas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='activities/'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
