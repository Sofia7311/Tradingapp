# Generated by Django 3.1.7 on 2021-04-22 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginpgm', '0014_auto_20210422_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresshistory',
            name='home_address_move_date',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Date Moved In'),
        ),
    ]
