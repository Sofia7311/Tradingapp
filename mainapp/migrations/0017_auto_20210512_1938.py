# Generated by Django 3.1.7 on 2021-05-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20210510_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='valid_from_date',
            field=models.DateField(verbose_name='Valid from date'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='valid_to_date',
            field=models.DateField(verbose_name='Valid to date'),
        ),
    ]