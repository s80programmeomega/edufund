# Generated by Django 5.1.7 on 2025-03-11 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorRepresentative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='images/school/representative/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('logo', models.ImageField(blank=True, upload_to='sponsors')),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('representative', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='sponsor.sponsorrepresentative')),
            ],
        ),
    ]
