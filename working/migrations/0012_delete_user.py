# Generated by Django 3.2.6 on 2021-12-03 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('working', '0011_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]