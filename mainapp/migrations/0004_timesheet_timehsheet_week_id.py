# Generated by Django 3.1.7 on 2021-07-27 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_timesheet_timehsheet_week_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='timehsheet_week_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.timesheetweek'),
            preserve_default=False,
        ),
    ]