# Generated by Django 5.1.7 on 2025-03-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
