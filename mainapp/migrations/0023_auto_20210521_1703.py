# Generated by Django 3.1.7 on 2021-05-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20210520_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheetweek',
            name='status',
            field=models.CharField(choices=[('PA', 'Pending Approval'), ('SUB', 'Submitted'), ('APPRVD', 'Approved'), ('REJECTED', 'Rejected')], max_length=20),
        ),
    ]