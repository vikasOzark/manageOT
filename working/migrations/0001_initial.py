# Generated by Django 3.2.6 on 2021-11-24 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(default='', max_length=250)),
                ('emp_l_name', models.CharField(default='', max_length=250)),
                ('emp_email', models.EmailField(default='', max_length=250)),
                ('emp_number', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OverTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overTime', models.FloatField(blank=True, null=True)),
                ('reaion', models.CharField(blank=True, max_length=250, null=True)),
                ('date_ot', models.DateTimeField(blank=True, null=True)),
                ('emp_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='working.employee')),
            ],
        ),
    ]