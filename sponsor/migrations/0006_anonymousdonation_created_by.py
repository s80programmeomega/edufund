# Generated by Django 5.1.7 on 2025-03-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_remove_anonymousdonation_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousdonation',
            name='created_by',
            field=models.CharField(blank=True, default='Anonymous User', editable=False, max_length=20),
        ),
    ]
