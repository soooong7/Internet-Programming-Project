# Generated by Django 3.1.1 on 2023-12-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20231201_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
