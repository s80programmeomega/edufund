# Generated by Django 5.1.7 on 2025-03-16 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousdonation',
            name='funding_campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='anonymous_donations', to='school.fundingcampaign'),
        ),
        migrations.AddField(
            model_name='donation',
            name='funding_campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='donations', to='school.fundingcampaign'),
        ),
    ]
