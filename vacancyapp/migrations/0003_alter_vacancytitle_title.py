# Generated by Django 4.2.5 on 2023-09-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyapp', '0002_alter_job_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancytitle',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
