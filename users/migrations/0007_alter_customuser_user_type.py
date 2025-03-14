# Generated by Django 5.1.7 on 2025-03-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('STAFF', 'Staff'), ('ADMIN', 'Admin'), ('SCHOOL', 'School'), ('SPONSOR', 'Sponsor'), ('GUEST', 'Guest')], default='STAFF', max_length=20),
        ),
    ]
