# Generated by Django 3.1.7 on 2021-04-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_timesheet_weekdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='weekdates',
            field=models.CharField(max_length=40, verbose_name='Start Date'),
        ),
    ]