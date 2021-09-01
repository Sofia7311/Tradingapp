# Generated by Django 3.1.7 on 2021-08-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210803_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheetweek',
            name='week_date_format',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='expense_type',
            field=models.CharField(choices=[('', 'Select Expense Type'), ('TRVL', 'Travel Expense'), ('TAXI', 'Taxi'), ('PARK', 'Parking'), ('CARM', 'Car Mileage'), ('POST', 'Postage'), ('PRNT', 'Print and Stationery'), ('BOOK', 'Books'), ('NEWS', 'News and Magazine'), ('SUBS', 'Subsistence'), ('HOME', 'Use of Home'), ('MEAL', 'Evening Meals'), ('HOTL', 'Hotels')], max_length=100),
        ),
    ]