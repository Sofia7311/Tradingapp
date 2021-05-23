from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainapp.models import CustomUser


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    date_of_birth   =   forms.DateField(widget=DateInput)
    date_of_joining =   forms.DateField(widget=DateInput)
    home_address_move_date  =   forms.DateField(widget=DateInput, help_text='Enter the date when you first moved in to the above address')

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'home_address', 
        'home_address_move_date','contact_number', 'job_title', 'department_name', 'work_eligibility', 'salary_initial', 
        'date_of_joining', 'national_insurance_number', 'emergency_contact_name', 'emergency_contact_number', 
        'emergency_contact_address', 'emergency_contact_relationship', 'bank_account_number', 'bank_sort_code')