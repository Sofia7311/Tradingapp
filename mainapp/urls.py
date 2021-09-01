from django.urls import path
from . import views
from .views import ExpenseAddView, ExpenseListView, ExpenseHomeView


urlpatterns = [
    path('',views.index,name="Index"),
    #path('search',views.search,name='search')
    path('add_timesheet', views.add_timesheet, name="add_timesheet"),
    path('user_timesheet', views.timesheet, name="user_timesheet"),
    path('update_timesheet/<int:pk>/', views.update_timesheet, name="update_timesheet"),
    path('add_expenses', views.add_expenses, name="add_expenses"),
    path('expenses_list', views.expenses_list, name="expenses_list"),
    path('home_expense', ExpenseHomeView.as_view(), name="home_expense"),
    path('add_expense', ExpenseAddView.as_view(), name="add_expense"),
    path('list_expense', ExpenseListView.as_view(), name="list_expense"),
]