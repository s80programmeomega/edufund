# Generated by Django 5.1.7 on 2025-03-20 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0006_anonymousdonation_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymousdonation',
            name='created_by',
            field=models.CharField(blank=True, default='Anonymous User', editable=False, max_length=200),
        ),
    ]
