# Generated by Django 3.1.7 on 2021-04-26 12:56

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210426_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
