# Generated by Django 3.1.7 on 2021-04-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210427_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='total_hours',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]