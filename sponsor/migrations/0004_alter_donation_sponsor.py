# Generated by Django 5.1.7 on 2025-03-11 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='donations', to='sponsor.sponsor'),
        ),
    ]
