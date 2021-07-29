from django import forms    
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mainapp.models import CustomUser, TimeSheet, CountryField, TimeSheetWeek
from loginpgm.models import AddressHistory
from django.utils import timezone
#from mainapp.countries import CountryField
#from django_countries.fields import CountryField
from django.utils.translation import ugettext as _


class DateInput(forms.DateInput):
    input_type = 'date'

class DateSelector(forms.MultiWidget):
    months = [(month, month) for month in range(1, 13)]
    widgets = [forms.SelectMultiple(choices=months),]


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=DateInput)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2','first_name', 'middle_name', 'last_name', 'date_of_birth','contact_number')


class CustomUserChangeForm(forms.ModelForm):
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
    #date_of_birth = forms.DateField(widget=DateInput)
    home_address_move_date = forms.DateField(widget=DateInput)
    #date_of_joining = forms.DateField(widget=DateInput)
    #nationality = forms.ChoiceField(choices=COUNTRIES)
    #nationality = CountryField(blank_label='(select country)')

    class Meta:
        model = CustomUser
        fields = ('home_address', 'home_address_move_date', 'emergency_contact_name', 'emergency_contact_number', 
        'emergency_contact_address', 'emergency_contact_relationship', 'bank_account_number', 'bank_sort_code')


class ReadonlyChangeForm(forms.ModelForm):
    home_address                    =   forms.CharField(disabled=True)
    home_address_move_date          =   forms.CharField(disabled=True)
    emergency_contact_name          =   forms.CharField(disabled=True)
    emergency_contact_number        =   forms.CharField(disabled=True)
    emergency_contact_address       =   forms.CharField(disabled=True)
    emergency_contact_relationship  =   forms.CharField(disabled=True)
    bank_account_number             =   forms.CharField(disabled=True)
    bank_sort_code                  =   forms.CharField(disabled=True)
    job_title                       =   forms.CharField(disabled=True)
    department_name                 =   forms.CharField(disabled=True)
    salary_initial                  =   forms.CharField(disabled=True)
    date_of_joining                 =   forms.CharField(disabled=True)
    national_insurance_number       =   forms.CharField(disabled=True)
    residence_permit_number         =   forms.CharField(disabled=True)
    visa_type                       =   forms.CharField(disabled=True)
    valid_from_date                 =   forms.CharField(disabled=True)
    valid_to_date                   =   forms.CharField(disabled=True)
    
    class Meta:
        model = CustomUser
        fields = ('home_address', 'home_address_move_date', 'emergency_contact_name', 'emergency_contact_number', 
        'emergency_contact_address', 'emergency_contact_relationship', 'bank_account_number', 'bank_sort_code',
        'job_title', 'department_name', 'salary_initial', 'date_of_joining', 'national_insurance_number', 'nationality',
        'residence_permit_number', 'visa_type',  'valid_from_date', 'valid_to_date')

class CustomUserJobForm(forms.ModelForm):
#date_of_birth = forms.DateField(widget=DateInput)
    home_address_move_date = forms.DateField(widget=DateInput)
    date_of_joining = forms.DateField(widget=DateInput)
    #nationality = forms.ChoiceField(choices=COUNTRIES)
    #nationality = CountryField(blank_label='(select country)')

    class Meta:
        model = CustomUser
        fields = ('job_title', 'department_name', 'salary_initial', 
        'date_of_joining', 'national_insurance_number', 'nationality')


class HomeAddressAdminChangeForm(forms.ModelForm):
    home_address_move_date   =   forms.DateField(widget=DateInput)
    
    class Meta:
        model = AddressHistory
        fields = ('home_address', 'home_address_move_date', 'home_address_move_out_date', 'addresshistory')


class HomeAddressChangeForm(forms.ModelForm):
    home_address_move_date   =   forms.DateField(widget=DateInput, label = 'New Address Move-in date')

    class Meta:
        model = AddressHistory
        fields = ('home_address', 'home_address_move_date')
    

class TimeSheetForm(forms.ModelForm):
    work_hours  =   forms.DecimalField(required=False)
    #status      =   forms.CharField(required=False)
    #total_hours =   forms.DecimalField(required=False)
    #project_id  =   forms.CharField(disabled=True)
    
    class Meta:
        model = TimeSheet
        fields = ('project_id','weekdates', 'work_hours', 'userid', 'status',  'timesheet_week_id')   


class TimeSheetWeekForm(forms.ModelForm):
    #weekdates   =   forms.DateField(disabled=True)
    #project_id  =   forms.CharField(disabled=True)
    
    class Meta:
        model = TimeSheetWeek
        fields = ('weekdates', 'status', 'total_hours', 'user_id') 

class TimeSheetStatusForm(forms.ModelForm):
    weekdates   =   forms.DateField(disabled=True)
    status      =   forms.CharField(disabled=True)
    total_hours =   forms.DecimalField(disabled=True)
    user_id     =   forms.CharField(disabled=True)
    
    class Meta:
        
        model = TimeSheetWeek
        fields = ('weekdates', 'status', 'total_hours', 'user_id') 

class VisaholderForm(forms.ModelForm):
    residence_permit_number =   forms.CharField(label = 'Biometric Residence Permit number')
    valid_from_date =   forms.DateField(widget=DateInput)
    valid_to_date   =   forms.DateField(widget=DateInput)
    class Meta:     
        model = CustomUser
        fields = ('residence_permit_number', 'visa_type',  'valid_from_date', 'valid_to_date')

class BritishPassportform(forms.ModelForm):
    residence_permit_number =   forms.CharField(label = 'British Passport number')
    valid_from_date =   forms.DateField(widget=DateInput)
    valid_to_date   =   forms.DateField(widget=DateInput)
    class Meta:     
        model = CustomUser
        fields = ('residence_permit_number', 'valid_from_date', 'valid_to_date')