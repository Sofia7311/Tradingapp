# Generated by Django 3.1.7 on 2021-04-27 10:03

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210426_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=746, multiple=True),
        ),
    ]