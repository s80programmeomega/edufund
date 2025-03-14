# Generated by Django 5.1.7 on 2025-03-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_alter_fundingcampaign_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='student_story',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
