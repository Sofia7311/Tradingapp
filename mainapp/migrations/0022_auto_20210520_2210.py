# Generated by Django 3.1.7 on 2021-05-20 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20210519_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='timesheetweek',
            name='status',
            field=models.CharField(choices=[('PG', 'Pending'), ('SUB', 'Submitted'), ('APPRVD', 'Approved'), ('SVD', 'Saved')], max_length=20),
        ),
    ]