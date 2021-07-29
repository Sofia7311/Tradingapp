from mainapp.forms import TimeSheetForm, TimeSheetWeekForm,  TimeSheetStatusForm
import xml.etree.ElementTree as ET
#from bs4 import BeautifulSoup as soup
#import requests
#from selenium import webdriver
#from mainapp.forms import TimeSheetForm
from .models import  TimeSheet, CustomUser, TimeSheetWeek
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def timesheet(request):

    save_count      =   TimeSheetWeek.objects.filter(status = 'SAVED', user_id=request.user).count()
    reject_count    =   TimeSheetWeek.objects.filter(status = 'REJECTED', user_id=request.user).count()
    submit_count    =   TimeSheetWeek.objects.filter(status = 'SUBMITTED', user_id=request.user).count()
    approve_count   =   TimeSheetWeek.objects.filter(status = 'APPROVED', user_id=request.user).count()

    if request.method == 'POST':
        if 'Save' in request.POST:
           # max_num_count = save_count
            current_status = 'SAVED'
        elif 'Submit' in request.POST:
           # max_num_count = submit_count
            current_status = 'SUBMITTED'
        elif 'Reject' in request.POST:
           # max_num_count = reject_count
            current_status = 'REJECTED'
        elif 'Approve' in request.POST:
            #max_num_count = approve_count
            current_status = 'APPROVED'
        else:
            current_status  =  ' '
            #
            # max_num_count  =  0                       

        '''if current_status == 'SAVED' or current_status == 'REJECTED':
            TimeSheetStatusFormset = formset_factory(TimeSheetWeekForm, max_num=max_num_count)
        else:
            TimeSheetStatusFormset = formset_factory(TimeSheetStatusForm, max_num=max_num_count)'''

        
        initial_data   = []
        try:
            #customuser_data = CustomUser.objects.get(email=request.user)
            # customuser_data = TimeSheetWeek.objects.filter(user_id=request.user, status=current_status)
            #timesheet_data = customuser_data.timesheetweek_set.all()
            #print(current_status)
            initial_data = TimeSheetWeek.objects.filter(status=current_status)
            #print('timesheet_instance:', initial_data)
            #TimeSheetWeek.objects.get(user_id=request.user, status=current_status)
        except CustomUser.DoesNotExist:
            initial_data = None
    
        '''for data in customuser_data:
            initial_data.append({'weekdates':data.weekdates,
                            'status' : data.status,
                            'total_hours': data.total_hours,
                            'user_id':  data.user_id
                            })'''

        #formset = TimeSheetStatusFormset(initial=initial_data)
        #print(formset)
        #return render(request, 'timesheet_status.html', {'formset': formset, 'status' :current_status, 'timesheet': timesheet_data})
        return render(request, 'timesheet_status.html', {'status' :current_status, 'timesheet': initial_data})
    else:
        week_day=datetime.datetime.now().isocalendar()[2]
        start_date=datetime.datetime.now() - datetime.timedelta(days=week_day+6)
        date_match = (start_date + datetime.timedelta(days=0)).date().strftime("%a") + ', ' + str((start_date + datetime.timedelta(days=0)).date())
        print('inside timesheet')
        print(date_match)
        try:
            timesheet_instance  = TimeSheetWeek.objects.get(user_id=request.user, weekdates=date_match)
            status =  timesheet_instance.status
        except TimeSheetWeek.DoesNotExist:
            try:
                timesheet_instance  = TimeSheet.objects.get(userid=request.user, weekdates=date_match)
                status =  timesheet_instance.status
            except TimeSheet.DoesNotExist:
                status =  'Not Submitted'

    
        return render(request, 'user_timesheet.html',  {'start_date': start_date, 'status':status, 'save_count': save_count,
                                                    'reject_count': reject_count, 'submit_count': submit_count,
                                                    'approve_count': approve_count})

@login_required
def add_timesheet(request):
    TimeSheetFormSet = inlineformset_factory(TimeSheetWeek, TimeSheet, fields=('project_id', 'work_hours', 'weekdates'), extra=7, max_num=7)
    
    week_day=datetime.datetime.now().isocalendar()[2]
    start_date=datetime.datetime.now() - datetime.timedelta(days=week_day+6)
    date_match = (start_date + datetime.timedelta(days=0)).date().strftime("%a") + ', ' + str((start_date + datetime.timedelta(days=0)).date())

    try:
        weektime_instance = TimeSheetWeek.objects.get(user_id=request.user, weekdates = date_match)
    except TimeSheetWeek.DoesNotExist:
        weektime_instance = None
    timesheetweek_instance   =   TimeSheetWeek.objects.last()
    print(timesheetweek_instance.id)
    #print(weektime_instance.id)
    if request.method == 'POST':
        print('inside add timesheet post')
        total_hours  =   0
        if weektime_instance is None:
            weektime_instance =  TimeSheetWeek()
            weektime_instance.total_hours = total_hours
            weektime_instance.weekdates   =  date_match
            weektime_instance.user_id =  request.user
            if 'Submit' in request.POST:
                weektime_instance.status = 'SUBMITTED'
            else:
                weektime_instance.status = 'SAVED'
            weektime_instance.save()
        else:
            weektime_instance.total_hours = total_hours
            weektime_instance.weekdates   =  date_match
            if 'Submit' in request.POST:
                weektime_instance.status = 'SUBMITTED'
            else:
                weektime_instance.status = 'SAVED'
            #weektime_instance.status  =  
            weektime_instance.save()
            
        if 'Save' in request.POST:
            formset = TimeSheetFormSet(request.POST, instance=weektime_instance)
            total_hours = 0
            
            print(weektime_instance.id)
            if formset.is_valid():
                
                for form in  formset:
                    work_instance =  form.save(commit=False)
                    total_hours +=   work_instance.work_hours
                    work_instance.status = 'SAVED'
                    work_instance.userid = request.user
                    work_instance.total_hours = total_hours
                    #work_instance.timesheet_week_id  =  weektime_instance.id
                    work_instance.save()
                weektime_instance.total_hours = total_hours
                weektime_instance.save()
                messages.success(request, f'Timesheet saved.')
            else:
                return render(request, 'add_timesheet.html', {'formset': formset})

        if 'Submit' in request.POST:
            formset = TimeSheetFormSet(request.POST, instance=weektime_instance)
            total_hours = 0
            
            if formset.is_valid():
                for form in  formset:
                    work_instance =  form.save(commit=False)
                    total_hours +=   work_instance.work_hours
                    #work_instance.status = 'SUBMITTED'
                    #work_instance.userid = request.user
                    #work_instance.save()
                    work_instance.delete()
                weektime_instance.total_hours = total_hours
                weektime_instance.save()
                #TimeSheet.objects.filter(userid=request.user).delete()
                messages.success(request, f'Timesheet Submitted.')
               # return redirect('user_timesheet')
            else:
                return render(request, 'add_timesheet.html', {'formset': formset})

        print(work_instance.status)
        
        return render(request, 'user_timesheet.html', {'status':work_instance.status, 'start_date': start_date})
                
    else:
        form =  TimeSheetWeekForm(request.POST)
        #print(form)
        initial_data = []
        print(start_date)
    
        for i in range(7):
            i +=  1
            print('i:',  i)
            dates=[(start_date + datetime.timedelta(days=i)).date().strftime("%a") + ', ' + 
                    str((start_date + datetime.timedelta(days=i)).date()) for i in range(7)]  

        for date_field in dates:
            initial_data.append({'weekdates':date_field,
                                'project_id': 'project890' })  
         
        '''if userid_data is None:
            customuser_data = None'''
        print(initial_data)
        formset = TimeSheetFormSet(initial=initial_data, instance=weektime_instance)  
        return render(request, 'add_timesheet.html', {'formset': formset})

@login_required
def update_timesheet(request, pk):
    TimeSheetFormSet = inlineformset_factory(TimeSheetWeek, TimeSheet, fields=('project_id', 'work_hours', 'weekdates', 'userid'), extra=7, max_num=7)
    
    week_timesheet = TimeSheetWeek.objects.get(id=pk)
    
    week_day=datetime.datetime.now().isocalendar()[2]
    start_date=datetime.datetime.now() - datetime.timedelta(days=week_day)
            
    try:
       weektime_instance = TimeSheetWeek.objects.get(user_id=request.user, weekdates = week_timesheet.weekdates)
    except TimeSheetWeek.DoesNotExist:
        weektime_instance = None

    print(weektime_instance)
    if request.method == 'POST':
        if 'Save' in request.POST:
            formset = TimeSheetFormSet(request.POST, instance=weektime_instance)
            total_hours = 0

            if formset.is_valid():
                for form in  formset:
                    work_instance =  form.save(commit=False)
                    total_hours +=   work_instance.work_hours
                    work_instance.status = 'SAVED'
                    work_instance.userid = request.user
                    work_instance.total_hours = total_hours
                    work_instance.save()
                messages.success(request, f'Timesheet saved.')
            else:
                return render(request, 'update_timesheet.html', {'formset': formset})

        if 'Submit' in request.POST:
            formset = TimeSheetFormSet(request.POST, instance=weektime_instance)
            total_hours = 0
            
            if formset.is_valid():
                for form in  formset:
                    work_instance =  form.save(commit=False)
                    total_hours +=   work_instance.work_hours
                    #work_instance.status = 'SUBMITTED'
                    #work_instance.userid = request.user
                    #work_instance.save()
                #TimeSheet.objects.filter(userid=request.user,weekdates = week_timesheet.weekdates).delete()
                    work_instance.delete()
                messages.success(request, f'Timesheet Submitted.')
            else:
                return render(request, 'add_timesheet.html', {'formset': formset})


        if weektime_instance is None:
            weektime_instance =  TimeSheetWeek()
            weektime_instance.total_hours = total_hours
            weektime_instance.weekdates = week_timesheet.weekdates
            weektime_instance.user_id =  request.user
            if 'Submit' in request.POST:
                weektime_instance.status = 'SUBMITTED'
            else:
                weektime_instance.status = 'SAVED'
            weektime_instance.save()
        else:
            weektime_instance.total_hours = total_hours
            weektime_instance.weekdates = week_timesheet.weekdates
            if 'Submit' in request.POST:
                weektime_instance.status = 'SUBMITTED'
            else:
                weektime_instance.status = 'SAVED'
            weektime_instance.save()
        return render(request, 'user_timesheet.html', {'status':work_instance.status, 'start_date': start_date})
    else:
        
        initial_data = []
        if  weektime_instance.status ==  'SAVED':
            selected_timesheet = TimeSheet.objects.get(weekdates=week_timesheet.weekdates)
            for i in range(7):
                selected_timesheet_id = TimeSheet.objects.get(id=selected_timesheet.id)
                initial_data.append({'weekdates':selected_timesheet_id.weekdates,
                             'project_id':selected_timesheet_id.project_id,
                            'status' : selected_timesheet_id.status,
                            'work_hours': selected_timesheet_id.work_hours,
                            
                            })
            
                i += 1
        else:
            for i in range(7):
                i +=  1
                print('i:',  i)
                dates=[(start_date + datetime.timedelta(days=i)).date().strftime("%a") + ', ' + 
                    str((start_date + datetime.timedelta(days=i)).date()) for i in range(7)]  

            for date_field in dates:
                initial_data.append({'weekdates':date_field,
                                'project_id': 'project890' })  


        formset = TimeSheetFormSet(instance=weektime_instance, initial = initial_data) 
         
        return render(request, 'update_timesheet.html', {'formset': formset})

#def search(request):

#    return render(request, 'index.html')
