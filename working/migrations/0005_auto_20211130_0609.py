# Generated by Django 3.2.6 on 2021-11-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working', '0004_alter_overtime_date_ot'),
    ]

    operations = [
        migrations.AddField(
            model_name='overtime',
            name='time_ot',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='date_ot',
            field=models.DateField(blank=True, null=True),
        ),
    ]