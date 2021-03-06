# Generated by Django 3.1.7 on 2021-08-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_expenses_is_standard_vat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expense_type',
            field=models.CharField(choices=[('', 'Select Expense Type'), ('Travel Expense', 'Travel Expense'), ('Taxi', 'Taxi'), ('Parking', 'Parking'), ('Car Mileage', 'Car Mileage'), ('Postage', 'Postage'), ('Print and Stationery', 'Print and Stationery'), ('Books', 'Books'), ('News and Magazine', 'News and Magazine'), ('Subsistence', 'Subsistence'), ('Use of Home', 'Use of Home'), ('Evening Meals', 'Evening Meals'), ('Hotels', 'Hotels')], max_length=100),
        ),
    ]
