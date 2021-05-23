from mainapp.forms import TimeSheetForm
import xml.etree.ElementTree as ET
#from bs4 import BeautifulSoup as soup
#import requests
#from selenium import webdriver
#from mainapp.forms import TimeSheetForm
from .models import  TimeSheet, CustomUser, TimeSheetWeek
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def timesheet(request):

    week_day=datetime.datetime.now().isocalendar()[2]
    start_date=datetime.datetime.now() - datetime.timedelta(days=week_day)
    date_match = (start_date + datetime.timedelta(days=0)).date().strftime("%a") + ', ' + str((start_date + datetime.timedelta(days=0)).date())
    print(date_match)

    try:
        timesheet_instance  = TimeSheetWeek.objects.get(user_id=request.user)
        status =  timesheet_instance.status
    except TimeSheetWeek.DoesNotExist:
        try:
            timesheet_instance  = TimeSheet.objects.get(userid=request.user, weekdates=date_match)
            status =  timesheet_instance.status
        except TimeSheet.DoesNotExist:
            status =  'Not Submitted'



    return render(request, 'user_timesheet.html',  {'start_date': start_date, 'status':status})



@login_required
def add_timesheet(request):
    TimeSheetFormSet = inlineformset_factory(CustomUser, TimeSheet, fields=('project_id', 'work_hours', 'weekdates'), form=TimeSheetForm, extra=7, max_num=7)
    week_day=datetime.datetime.now().isocalendar()[2]
    start_date=datetime.datetime.now() - datetime.timedelta(days=week_day)
    current_date = (start_date + datetime.timedelta(days=week_day)).date().strftime("%a") + ', ' + str((start_date + datetime.timedelta(days=week_day)).date())
    try:
        userid_data = TimeSheet.objects.get(userid=request.user, weekdates = current_date)
    except TimeSheet.DoesNotExist:
        userid_data = None    

    try:
        customuser_data = CustomUser.objects.get(email=request.user)
    except CustomUser.DoesNotExist:
        customuser_data = None
    
    if request.method == 'POST':
        if 'Save' in request.POST:
            formset = TimeSheetFormSet(request.POST, instance=customuser_data)
            total_hours = 0
            print(formset)

            if formset.is_valid():
                for form in  formset:
                    work_instance =  form.save(commit=False)
                    total_hours +=   work_instance.work_hours
                    work_instance.status = 'Saved'
                    work_instance.userid = request.user
                    work_instance.total_hours = total_hours
                    work_instance.save()
                messages.success(request, f'Timesheet saved.')
               # return render(request, 'user_timesheet.html', {'status':work_instance.status, 'start_date': start_date})
            else:
                return render(request, 'add_timesheet.html', {'formset': formset})

        if 'Submit' in request.POST:
            formset = TimeSheetFormSet(request.POST, instance=customuser_data)
            total_hours = 0
            
            if formset.is_valid():
                for form in  formset:
                    work_instance =  form.save(commit=False)
                    total_hours +=   work_instance.work_hours
                    work_instance.status = 'Submitted'
                    work_instance.userid = request.user
                    work_instance.save()
                TimeSheet.objects.filter(userid=request.user).delete()
                messages.success(request, f'Timesheet Submitted.')
               # return redirect('user_timesheet')
            else:
                return render(request, 'add_timesheet.html', {'formset': formset})
        try:
            weektime_instance = TimeSheetWeek.objects.get(user_id=request.user)
        except TimeSheetWeek.DoesNotExist:
            weektime_instance = None

        

        if weektime_instance is None:
            weektime_instance =  TimeSheetWeek()
            weektime_instance.total_hours = total_hours
            weektime_instance.weekdates   =  start_date
            weektime_instance.user_id =  request.user
            if 'Submit' in request.POST:
                weektime_instance.status = 'Submitted'
            else:
                weektime_instance.status = 'Saved'
            weektime_instance.save()
        else:
            weektime_instance.total_hours = total_hours
            if 'Submit' in request.POST:
                weektime_instance.status = 'Submitted'
            else:
                weektime_instance.status = 'Saved'
            #weektime_instance.status  =  
            weektime_instance.save()
        return render(request, 'user_timesheet.html', {'status':work_instance.status, 'start_date': start_date})
                
    else:
        initial_data = []
        next_week = False

        for i in range(7):
            dates=[(start_date + datetime.timedelta(days=i)).date().strftime("%a") + ', ' + 
                    str((start_date + datetime.timedelta(days=i)).date()) for i in range(7)]  

        for date_field in dates:
            initial_data.append({'weekdates':date_field,
                                'project_id':'Project123' })  
         
        if userid_data is None:
            customuser_data = None

        formset = TimeSheetFormSet(initial=initial_data, instance=customuser_data)  
        return render(request, 'add_timesheet.html', {'formset': formset})

#def search(request):
#    return render(request, 'index.html')
