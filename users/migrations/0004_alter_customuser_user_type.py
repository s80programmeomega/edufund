# Generated by Django 5.1.7 on 2025-03-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('SCHOOL', 'School'), ('SPONSOR', 'Sponsor')], max_length=20),
        ),
    ]
