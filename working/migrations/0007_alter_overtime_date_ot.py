# Generated by Django 3.2.6 on 2021-11-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working', '0006_remove_overtime_time_ot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='date_ot',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
