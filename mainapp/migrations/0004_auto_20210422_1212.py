# Generated by Django 3.1.7 on 2021-04-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_timesheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='home_address_move_date',
            field=models.DateField(verbose_name='Address Move Date'),
        ),
    ]