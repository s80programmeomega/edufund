# Generated by Django 5.1.7 on 2025-03-11 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_alter_donation_funding_campaign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='representative',
        ),
        migrations.AddField(
            model_name='sponsorrepresentative',
            name='sponsor',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='representative', to='sponsor.sponsor'),
            preserve_default=False,
        ),
    ]
