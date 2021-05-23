from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="Index"),
    #path('search',views.search,name='search')
    path('add_timesheet', views.add_timesheet, name="add_timesheet"),
    path('user_timesheet', views.timesheet, name="user_timesheet"),
    path('timesheet_status', views.timesheet, name="timesheet_status")
]