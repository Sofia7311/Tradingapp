
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime
from django.utils import timezone
from django.db import models
#from mainapp.countries import CountryField
from django_countries.fields import CountryField
from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    COUNTRIES = (
    ('', _('Select Country')),
    ('AD', _('Andorra')),
    ('AE', _('United Arab Emirates')),
    ('AF', _('Afghanistan')),
    ('AG', _('Antigua & Barbuda')),
    ('AI', _('Anguilla')),
    ('AL', _('Albania')),
    ('AM', _('Armenia')),
    ('AN', _('Netherlands Antilles')),
    ('AO', _('Angola')),
    ('AQ', _('Antarctica')),
    ('AR', _('Argentina')),
    ('AS', _('American Samoa')),
    ('AT', _('Austria')),
    ('AU', _('Australia')),
    ('AW', _('Aruba')),
    ('AZ', _('Azerbaijan')),
    ('BA', _('Bosnia and Herzegovina')),
    ('BB', _('Barbados')),
    ('BD', _('Bangladesh')),
    ('BE', _('Belgium')),
    ('BF', _('Burkina Faso')),
    ('BG', _('Bulgaria')),
    ('BH', _('Bahrain')),
    ('BI', _('Burundi')),
    ('BJ', _('Benin')),
    ('BM', _('Bermuda')),
    ('BN', _('Brunei Darussalam')),
    ('BO', _('Bolivia')),
    ('BR', _('Brazil')),
    ('BS', _('Bahama')),
    ('BT', _('Bhutan')),
    ('BV', _('Bouvet Island')),
    ('BW', _('Botswana')),
    ('BY', _('Belarus')),
    ('BZ', _('Belize')),
    ('CA', _('Canada')),
    ('CC', _('Cocos (Keeling) Islands')),
    ('CF', _('Central African Republic')),
    ('CG', _('Congo')),
    ('CH', _('Switzerland')),
    ('CI', _('Ivory Coast')),
    ('CK', _('Cook Iislands')),
    ('CL', _('Chile')),
    ('CM', _('Cameroon')),
    ('CN', _('China')),
    ('CO', _('Colombia')),
    ('CR', _('Costa Rica')),
    ('CU', _('Cuba')),
    ('CV', _('Cape Verde')),
    ('CX', _('Christmas Island')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DE', _('Germany')),
    ('DJ', _('Djibouti')),
    ('DK', _('Denmark')),
    ('DM', _('Dominica')),
    ('DO', _('Dominican Republic')),
    ('DZ', _('Algeria')),
    ('EC', _('Ecuador')),
    ('EE', _('Estonia')),
    ('EG', _('Egypt')),
    ('EH', _('Western Sahara')),
    ('ER', _('Eritrea')),
    ('ES', _('Spain')),
    ('ET', _('Ethiopia')),
    ('FI', _('Finland')),
    ('FJ', _('Fiji')),
    ('FK', _('Falkland Islands (Malvinas)')),
    ('FM', _('Micronesia')),
    ('FO', _('Faroe Islands')),
    ('FR', _('France')),
    ('FX', _('France, Metropolitan')),
    ('GA', _('Gabon')),
    ('GB', _('United Kingdom (Great Britain)')),
    ('GD', _('Grenada')),
    ('GE', _('Georgia')),
    ('GF', _('French Guiana')),
    ('GH', _('Ghana')),
    ('GI', _('Gibraltar')),
    ('GL', _('Greenland')),
    ('GM', _('Gambia')),
    ('GN', _('Guinea')),
    ('GP', _('Guadeloupe')),
    ('GQ', _('Equatorial Guinea')),
    ('GR', _('Greece')),
    ('GS', _('South Georgia and the South Sandwich Islands')),
    ('GT', _('Guatemala')),
    ('GU', _('Guam')),
    ('GW', _('Guinea-Bissau')),
    ('GY', _('Guyana')),
    ('HK', _('Hong Kong')),
    ('HM', _('Heard & McDonald Islands')),
    ('HN', _('Honduras')),
    ('HR', _('Croatia')),
    ('HT', _('Haiti')),
    ('HU', _('Hungary')),
    ('ID', _('Indonesia')),
    ('IE', _('Ireland')),
    ('IL', _('Israel')),
    ('IN', _('India')),
    ('IO', _('British Indian Ocean Territory')),
    ('IQ', _('Iraq')),
    ('IR', _('Islamic Republic of Iran')),
    ('IS', _('Iceland')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JO', _('Jordan')),
    ('JP', _('Japan')),
    ('KE', _('Kenya')),
    ('KG', _('Kyrgyzstan')),
    ('KH', _('Cambodia')),
    ('KI', _('Kiribati')),
    ('KM', _('Comoros')),
    ('KN', _('St. Kitts and Nevis')),
    ('KP', _('Korea, Democratic People\'s Republic of')),
    ('KR', _('Korea, Republic of')),
    ('KW', _('Kuwait')),
    ('KY', _('Cayman Islands')),
    ('KZ', _('Kazakhstan')),
    ('LA', _('Lao People\'s Democratic Republic')),
    ('LB', _('Lebanon')),
    ('LC', _('Saint Lucia')),
    ('LI', _('Liechtenstein')),
    ('LK', _('Sri Lanka')),
    ('LR', _('Liberia')),
    ('LS', _('Lesotho')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('LV', _('Latvia')),
    ('LY', _('Libyan Arab Jamahiriya')),
    ('MA', _('Morocco')),
    ('MC', _('Monaco')),
    ('MD', _('Moldova, Republic of')),
    ('MG', _('Madagascar')),
    ('MH', _('Marshall Islands')),
    ('ML', _('Mali')),
    ('MN', _('Mongolia')),
    ('MM', _('Myanmar')),
    ('MO', _('Macau')),
    ('MP', _('Northern Mariana Islands')),
    ('MQ', _('Martinique')),
    ('MR', _('Mauritania')),
    ('MS', _('Monserrat')),
    ('MT', _('Malta')),
    ('MU', _('Mauritius')),
    ('MV', _('Maldives')),
    ('MW', _('Malawi')),
    ('MX', _('Mexico')),
    ('MY', _('Malaysia')),
    ('MZ', _('Mozambique')),
    ('NA', _('Namibia')),
    ('NC', _('New Caledonia')),
    ('NE', _('Niger')),
    ('NF', _('Norfolk Island')),
    ('NG', _('Nigeria')),
    ('NI', _('Nicaragua')),
    ('NL', _('Netherlands')),
    ('NO', _('Norway')),
    ('NP', _('Nepal')),
    ('NR', _('Nauru')),
    ('NU', _('Niue')),
    ('NZ', _('New Zealand')),
    ('OM', _('Oman')),
    ('PA', _('Panama')),
    ('PE', _('Peru')),
    ('PF', _('French Polynesia')),
    ('PG', _('Papua New Guinea')),
    ('PH', _('Philippines')),
    ('PK', _('Pakistan')),
    ('PL', _('Poland')),
    ('PM', _('St. Pierre & Miquelon')),
    ('PN', _('Pitcairn')),
    ('PR', _('Puerto Rico')),
    ('PT', _('Portugal')),
    ('PW', _('Palau')),
    ('PY', _('Paraguay')),
    ('QA', _('Qatar')),
    ('RE', _('Reunion')),
    ('RO', _('Romania')),
    ('RU', _('Russian Federation')),
    ('RW', _('Rwanda')),
    ('SA', _('Saudi Arabia')),
    ('SB', _('Solomon Islands')),
    ('SC', _('Seychelles')),
    ('SD', _('Sudan')),
    ('SE', _('Sweden')),
    ('SG', _('Singapore')),
    ('SH', _('St. Helena')),
    ('SI', _('Slovenia')),
    ('SJ', _('Svalbard & Jan Mayen Islands')),
    ('SK', _('Slovakia')),
    ('SL', _('Sierra Leone')),
    ('SM', _('San Marino')),
    ('SN', _('Senegal')),
    ('SO', _('Somalia')),
    ('SR', _('Suriname')),
    ('ST', _('Sao Tome & Principe')),
    ('SV', _('El Salvador')),
    ('SY', _('Syrian Arab Republic')),
    ('SZ', _('Swaziland')),
    ('TC', _('Turks & Caicos Islands')),
    ('TD', _('Chad')),
    ('TF', _('French Southern Territories')),
    ('TG', _('Togo')),
    ('TH', _('Thailand')),
    ('TJ', _('Tajikistan')),
    ('TK', _('Tokelau')),
    ('TM', _('Turkmenistan')),
    ('TN', _('Tunisia')),
    ('TO', _('Tonga')),
    ('TP', _('East Timor')),
    ('TR', _('Turkey')),
    ('TT', _('Trinidad & Tobago')),
    ('TV', _('Tuvalu')),
    ('TW', _('Taiwan, Province of China')),
    ('TZ', _('Tanzania, United Republic of')),
    ('UA', _('Ukraine')),
    ('UG', _('Uganda')),
    ('UM', _('United States Minor Outlying Islands')),
    ('US', _('United States of America')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('VA', _('Vatican City State (Holy See)')),
    ('VC', _('St. Vincent & the Grenadines')),
    ('VE', _('Venezuela')),
    ('VG', _('British Virgin Islands')),
    ('VI', _('United States Virgin Islands')),
    ('VN', _('Viet Nam')),
    ('VU', _('Vanuatu')),
    ('WF', _('Wallis & Futuna Islands')),
    ('WS', _('Samoa')),
    ('YE', _('Yemen')),
    ('YT', _('Mayotte')),
    ('YU', _('Yugoslavia')),
    ('ZA', _('South Africa')),
    ('ZM', _('Zambia')),
    ('ZR', _('Zaire')),
    ('ZW', _('Zimbabwe')),
    ('ZZ', _('Unknown or unspecified country')),
    )

    UK_VISA_TYPES  =   [
        ('T1', 'Tier 1 (General) visa'),
        ('T2', 'Tier 1 (Exceptional Talent) visa'),
        ('T3', 'Tier 1 (Investor) visa'),
        ('T4', 'Tier 1 (Entrepreneur) visa'),
        ('T5', 'Highly Skilled Migrant Programme'),
        ('T6', 'Tier 2 (General) visa'),
        ('T7', 'Tier 2 (Minister of Religion) visa'),
        ('T8', 'Tier 2 (Sportsperson) visa'),
        ('T9', 'Tier 2 (Intra-Company Transfer) visa'),
        ('T10', 'Tier 4 (Child) Student Visa'),
        ('T11', 'Tier 4 (General) Student Visa'),
        ('T12', 'Short Term Study Visa'),
        ('T13', 'Tier 5 (Youth Mobility Scheme) Visa'),
        ('T14', 'Tier 5 (Temporary Worker) Visa'),
        ('T15', 'Turkish Businessperson or Turkish Worker visa'),
        ('T16', 'Work Permit'),
        ('T17', 'Sole Representative of an Overseas Business visa'),
        ('T18', 'Representative of an Overseas Newspaper, News Agency or Broadcaster visa'),
        ('T19', 'Domestic Worker visa'),
        ('T20', 'Skilled Worker visa'),
        ('T21', 'Global Talent visa'),
        ('T22', 'Innovator visa'),
        ('T23', 'Marriage Visitor Visa'),
        ('T24', 'Parent of a Tier 4 (Child) Student Visa'),
        ('T25', 'Permitted Paid Engagement Visa'),
        ('T26', 'Short-term Study Visa'),
        ('T27', 'UK Visitor Visa'),
        ('T28', 'Visa for a Chinese Tour Group'),
        ('T29', 'UK Spouse Visa'),
        ('T30', 'UK Parent Visa'),
        ('T31', 'UK Child Visa'),
        ('Other', 'Other')
        ] 

    email                       =   models.EmailField(primary_key=True, verbose_name='Email address', max_length=255, unique=True, error_messages={'unique': 'Email address already exists.'})
    username                    =   models.CharField(blank=True, max_length=150, verbose_name='username')
    middle_name                 =   models.CharField(blank=True, max_length = 150)
    home_address                =   models.CharField(max_length = 200)
    national_insurance_number   =   models.CharField(max_length = 20)
    department_name             =   models.CharField(max_length = 200)
    job_title                   =   models.CharField(max_length = 100)
    salary_initial              =   models.CharField(max_length = 20, verbose_name='Starting salary')
    bank_account_number         =   models.CharField(max_length = 20, verbose_name = 'Account number')
    contact_number              =   models.CharField(max_length = 20)
    date_of_birth               =   models.DateField(verbose_name='Date of Birth', default=timezone.now)
    bank_sort_code              =   models.CharField(max_length = 10, verbose_name = 'Sort Code')
    emergency_contact_name      =   models.CharField(max_length = 200, verbose_name = 'Name')
    emergency_contact_number    =   models.CharField(max_length = 20, verbose_name = 'Contact number')
    emergency_contact_address   =   models.CharField(max_length = 200, verbose_name = 'Address')
    date_joined                 =   models.DateTimeField(default=timezone.now, verbose_name='Logged in date')
    date_of_joining             =   models.DateField(verbose_name='Date of joining', null=True)
    first_name                  =   models.CharField(max_length=150)
    last_name                   =   models.CharField(max_length=150)
    emergency_contact_relationship  =   models.CharField(max_length=150)
    home_address_move_date          =   models.DateField(verbose_name='Address Move Date', null=True)
    nationality                     =   models.CharField(max_length = 20, choices=COUNTRIES)
    residence_permit_number         =   models.CharField(max_length = 50)
    valid_from_date                 =   models.DateField(verbose_name='Valid from date', null=True)
    valid_to_date                   =   models.DateField(verbose_name='Valid to date', null=True)
    visa_type                       =   models.CharField(max_length = 100, choices=UK_VISA_TYPES)
    visa_attachment                 =   models.ImageField(upload_to = 'images/', null=True, blank=True)
    passport_attachment             =   models.ImageField(upload_to = 'images/', null=True, blank=True)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return self.email


class TimeSheetWeek(models.Model):
    STATUS_CHOICES  =   [
        ('SAVED', 'Saved'),
        ('PENDING APRROVAL', 'Pending Approval'),
        ('SUBMITTED', 'Submitted'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
        ] 
    #id =   models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    weekdates   =   models.CharField(max_length = 40, verbose_name='Start Date')
    #week_date_format  =  models.DateField()
    #timesheetweek_id  =   models.CharField(max_length = 40)
    total_hours =   models.DecimalField(max_digits=5, decimal_places=2)
    status      =   models.CharField(max_length = 20, choices=STATUS_CHOICES)
    user_id      =   models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank=True)

    def __int__(self):
        return self.id
        

class TimeSheet(models.Model):

    #weekdates   =   models.ForeignKey(TimeSheetWeek, on_delete = models.CASCADE, blank=True)
    weekdates   =   models.CharField(max_length = 40, verbose_name='Start Date')
    project_id  =   models.CharField(max_length = 50)
    work_hours  =   models.DecimalField(max_digits=5, decimal_places=2, null=True)
    total_hours =   models.DecimalField(max_digits=5, decimal_places=2, null=True)
    status      =   models.CharField(max_length = 20, null=True)
    timesheet_week_id =  models.ForeignKey(TimeSheetWeek, on_delete = models.CASCADE, blank=True)
    userid      =   models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank=True)

    def __int__(self):
        return self.id

class Expenses(models.Model):
    EXPENSE_CHOICES  =   [
        ('', 'Select Expense Type'),
        ('Travel Expense', 'Travel Expense'),
        ('Taxi', 'Taxi'),
        ('Parking', 'Parking'),
        ('Car Mileage', 'Car Mileage'),
        ('Postage', 'Postage'),
        ('Print and Stationery', 'Print and Stationery'),
        ('Books', 'Books'),
        ('News and Magazine', 'News and Magazine'),
        ('Subsistence', 'Subsistence'),
        ('Use of Home', 'Use of Home'),
        ('Evening Meals', 'Evening Meals'),
        ('Hotels', 'Hotels')

        ] 
    expense_type        =   models.CharField(max_length = 100,  choices=EXPENSE_CHOICES)
    expense_net         =   models.DecimalField(max_digits=6, decimal_places=2, null=True)
    is_standard_VAT     =   models.CharField(max_length=5)
    expense_VAT         =   models.DecimalField(max_digits=6, decimal_places=2, null=True)
    expense_gross       =   models.DecimalField(max_digits=6, decimal_places=2, null=True)
    comments            =   models.TextField(max_length = 150, null=True)
    expense_date        =   models.DateField()
    expense_update_date =   models.DateTimeField(default=timezone.now, verbose_name='Logged in date')
    expense_attachment  =   models.ImageField(upload_to = 'images/', null=True, blank=True)
    userid              =   models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.expense_type

