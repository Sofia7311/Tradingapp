from django import forms
from django.contrib import admin
from mainapp.models import CustomUser, TimeSheet, TimeSheetWeek
from loginpgm.models import AddressHistory
from mainapp.forms import CustomUserCreationForm, CustomUserChangeForm, HomeAddressAdminChangeForm, TimeSheetForm, TimeSheetWeekForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserInline(admin.TabularInline):
    model = AddressHistory

class CustomUserAdmin(UserAdmin):

    #inlines = [UserInline, ]

    #model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'job_title')
    #list_filter = ('is_admin',)
    fieldsets = (
        ('Personal info', {'fields': ('home_address',
        'home_address_move_date','contact_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Employment details', {'fields': ('job_title', 'department_name', 'salary_initial', 
        'date_of_joining', 'national_insurance_number')}),
        ('Emergency contact details', {'fields': ('emergency_contact_name', 'emergency_contact_number', 
        'emergency_contact_address')}),
        ('Bank Details', {'fields': ('bank_account_number', 'bank_sort_code')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    #readonly_fields = ()
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name','middle_name','last_name', 'date_of_birth'),
        }),
    )
    #search_fields = ('email',)
    #ordering = ('email',)
    #filter_horizontal = ()

class AddressHistoryAdmin(admin.ModelAdmin):


    class Meta:
        model = AddressHistory
        verbose_name_plural = 'Address Histories'


    form = HomeAddressAdminChangeForm
    list_display = ('home_address', 'home_address_move_date', 'home_address_move_out_date', 'addresshistory')
    #list_select_related  =  ('addresshistory',)
    ordering = ('addresshistory', 'home_address_move_date', )
    save_as = True


class TimeSheetAdmin(admin.ModelAdmin):

    class Meta:
        model = TimeSheet
        verbose_name_plural = 'Time sheets'


    form = TimeSheetForm
    list_display = ('id', 'project_id', 'userid', 'weekdates', 'timesheet_week_id', 'status')
    #list_select_related  =  ('addresshistory',)
    ordering = ('userid',)

class TimeSheetWeekAdmin(admin.ModelAdmin):

    class Meta:
        model = TimeSheetWeek
        verbose_name_plural = 'Week Timesheet'


    #form = TimeSheetWeekForm()
    list_display = ('user_id', 'weekdates', 'status', 'total_hours','week_date_format')
    #list_select_related  =  ('addresshistory',)
    ordering = ('user_id',)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(AddressHistory, AddressHistoryAdmin)
admin.site.register(TimeSheet, TimeSheetAdmin)
admin.site.register(TimeSheetWeek, TimeSheetWeekAdmin)