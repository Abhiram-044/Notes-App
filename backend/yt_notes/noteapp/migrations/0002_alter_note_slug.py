# Generated by Django 5.1.1 on 2025-03-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
