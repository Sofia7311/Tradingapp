# Generated by Django 3.1.7 on 2021-08-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210805_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='passport_attachment',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='visa_attachment',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='visa_type',
            field=models.CharField(choices=[('T1', 'Tier 1 (General) visa'), ('T2', 'Tier 1 (Exceptional Talent) visa'), ('T3', 'Tier 1 (Investor) visa'), ('T4', 'Tier 1 (Entrepreneur) visa'), ('T5', 'Highly Skilled Migrant Programme'), ('T6', 'Tier 2 (General) visa'), ('T7', 'Tier 2 (Minister of Religion) visa'), ('T8', 'Tier 2 (Sportsperson) visa'), ('T9', 'Tier 2 (Intra-Company Transfer) visa'), ('T10', 'Tier 4 (Child) Student Visa'), ('T11', 'Tier 4 (General) Student Visa'), ('T12', 'Short Term Study Visa'), ('T13', 'Tier 5 (Youth Mobility Scheme) Visa'), ('T14', 'Tier 5 (Temporary Worker) Visa'), ('T15', 'Turkish Businessperson or Turkish Worker visa'), ('T16', 'Work Permit'), ('T17', 'Sole Representative of an Overseas Business visa'), ('T18', 'Representative of an Overseas Newspaper, News Agency or Broadcaster visa'), ('T19', 'Domestic Worker visa'), ('T20', 'Skilled Worker visa'), ('T21', 'Global Talent visa'), ('T22', 'Innovator visa'), ('T23', 'Marriage Visitor Visa'), ('T24', 'Parent of a Tier 4 (Child) Student Visa'), ('T25', 'Permitted Paid Engagement Visa'), ('T26', 'Short-term Study Visa'), ('T27', 'UK Visitor Visa'), ('T28', 'Visa for a Chinese Tour Group'), ('T29', 'UK Spouse Visa'), ('T30', 'UK Parent Visa'), ('T31', 'UK Child Visa'), ('Other', 'Other')], max_length=100),
        ),
    ]