# Generated by Django 3.1.7 on 2021-04-15 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginpgm', '0006_auto_20210415_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresshistory',
            old_name='added_by',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='addresshistory',
            old_name='address_value',
            new_name='home_address',
        ),
        migrations.RenameField(
            model_name='addresshistory',
            old_name='address_from_date',
            new_name='home_address_move_date',
        ),
        migrations.RenameField(
            model_name='addresshistory',
            old_name='address_to_date',
            new_name='home_address_move_out_date',
        ),
    ]
