from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, User
#from loginpgm.forms import 
from mainapp.forms import CustomUserCreationForm, CustomUserChangeForm, HomeAddressChangeForm, ReadonlyChangeForm, VisaholderForm, BritishPassportform, CustomUserJobForm
from mainapp.forms import ReadonlyChangeForm
from mainapp.models import CustomUser
from loginpgm.models import AddressHistory
#from verify_email.email_handler import send_verification_email
from mainapp.confirm_email_verify import send_verification_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.utils.translation import gettext, gettext_lazy as _
from django.utils import timezone


class CustomAuthForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is not activated yet. Please activate your Email with the verification link sent to your Email address"),
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
    
            if self.user_cache is None:
               # self.user_cache = CustomUser.objects.get(email=username)
                try:
                    self.user_cache = CustomUser.objects.get(email=username)
                except CustomUser.DoesNotExist:
                    self.user_cache = None

                print('inside first if', self.user_cache)
                if self.user_cache is not None:
                    if CustomUser.objects.filter(email=username, is_active=True):
                        raise self.get_invalid_login_error()
                    else:
                        print('inside else')
                        self.confirm_login_allowed(self.user_cache)
                else:
                    raise self.get_invalid_login_error()
        
        return self.cleaned_data


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            send_verification_email(request, form)
            messages.success(request, f'Account created for {email}.A verification link has been sent to your email address. Please check and validate your email')
        return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form    =   CustomUserChangeForm(request.POST, instance=request.user)
    
        if 'Save' in request.POST:       
            if form.is_valid:
                form.save()

                try:
                    address_instance =  AddressHistory.objects.get(addresshistory=request.user, home_address_move_out_date__isnull=True)
                except AddressHistory.DoesNotExist:
                    address_instance = None

                if address_instance is None:
                    address_instance = AddressHistory()
                    address_instance.addresshistory =   request.user
                    address_instance.home_address =  request.POST['home_address']
                    address_instance.home_address_move_date = request.POST['home_address_move_date']
                    address_instance.save() 
            messages.success(request, f'Emergency contact details-update successful!!.')
        return redirect('profile_readonly')
    else:
        form    =   CustomUserChangeForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})

@login_required
def profile_readonly(request):
     
    if request.method == 'POST':
        form    =   ReadonlyChangeForm(request.POST, instance=request.user)
        print(request.POST)

        if 'Edit bank' in request.POST:
            return redirect('profile')
        elif 'Edit Address' in request.POST:       
            return redirect('home_address_update')
        elif 'Edit Job' in request.POST:    
            return redirect('user_job_details')
        elif 'Edit Nationality' in request.POST:   
            return redirect('nationality')
    else:
        form    =   ReadonlyChangeForm(instance=request.user)
    return render(request, 'profile_readonly.html', {'form': form})

@login_required
def user_job(request):
    #user_data = CustomUser.objects.get(id=pk_user)

    if request.method == 'POST':
        form    =   CustomUserJobForm(request.POST, instance=request.user)
                
        if form.is_valid:
            if 'Continue' in request.POST: 
                CustomUser.objects.filter(pk=request.user).update(
                    job_title = request.POST['job_title'], 
                    department_name = request.POST['department_name'],
                    salary_initial = request.POST[ 'salary_initial'],
                    date_of_joining = request.POST['date_of_joining'],
                    national_insurance_number = request.POST['national_insurance_number'],
                    nationality = request.POST['nationality']
                    )

                messages.success(request, f'Job details - update successful!!')
               # return render(request, 'user_job_details.html', {'form': form})
                return redirect('profile_readonly')
    else:
        form    =   CustomUserJobForm(instance=request.user)
        return render(request, 'user_job_details.html', {'form': form})


@login_required
def home_address_update(request):
    try:
        old_address_instance = AddressHistory.objects.get(
            addresshistory=request.user, 
            home_address_move_out_date__isnull=True)
    except AddressHistory.DoesNotExist:
        old_address_instance  =  None

    if request.method == 'POST':
        form    =   HomeAddressChangeForm(request.POST)
        
        if form.is_valid:
            if old_address_instance:
                #update existing address on AddressHistory DB
                old_address_instance.home_address_move_out_date = request.POST['home_address_move_date']
                old_address_instance.save()
                
                #update existing address on CustomUser table
                customuser_address = CustomUser.objects.get(pk=request.user)
                customuser_address.home_address = request.POST['home_address']
                customuser_address.home_address_move_date = request.POST['home_address_move_date']
                customuser_address.save()
                      

            #save new address instance as new record in AddressHistory DB
            address_instance = form.save(commit=False)
            address_instance.addresshistory = request.user
            address_instance.save()
            messages.success(request, f'Address update successful.')
            return redirect('profile_readonly')
    else:
        form    =   HomeAddressChangeForm()
        if old_address_instance:
            current_address = old_address_instance.home_address
        else:
            current_address = ' '
        return render(request, 'home_address_update.html', {'form': form, 'current_address': current_address} )

@login_required
def nationality(request):
    if request.method == 'POST':
        if 'Visa' in request.POST: 
            form = VisaholderForm(request.POST, request.FILES, instance=request.user)
            print(form)
            if form.is_valid:
                form.save()
                messages.success(request, f'Your profile details updated Successfully!')
                return redirect('profile_readonly') 
            else:
                #form = VisaholderForm(instance=request.user)
                return render(request, 'visaholder_form.html', {'form': form})

        if 'Passport' in request.POST: 
            form = BritishPassportform(request.POST, request.FILES, instance=request.user)

            if form.is_valid:
                form.save()
                messages.success(request, f'Your profile details updated Successfully!')
                return redirect('profile_readonly') 
            else:
                #form = BritishPassportform(instance=request.user)
                return render(request, 'British_passport_form.html', {'form': form})       
    else:
        try:
            uk_citizen = CustomUser.objects.get(nationality='GB')
        except CustomUser.DoesNotExist:
            uk_citizen = None
        if uk_citizen is not None:
            form = BritishPassportform(instance=request.user)
            return render(request, 'British_passport_form.html', {'form': form})
        else:
            form = VisaholderForm(instance=request.user)
            return render(request, 'visaholder_form.html', {'form': form})