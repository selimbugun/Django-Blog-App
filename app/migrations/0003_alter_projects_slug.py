# Generated by Django 5.1 on 2024-09-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_projects_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
