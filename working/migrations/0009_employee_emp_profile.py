# Generated by Django 3.2.6 on 2021-12-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working', '0008_alter_overtime_date_ot'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_profile',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
    ]