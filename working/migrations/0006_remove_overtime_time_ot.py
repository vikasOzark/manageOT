# Generated by Django 3.2.6 on 2021-11-30 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('working', '0005_auto_20211130_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overtime',
            name='time_ot',
        ),
    ]