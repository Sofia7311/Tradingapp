from django.urls import path
from . import views
from django.contrib.auth import views as user_views
from django.urls import reverse_lazy


urlpatterns = [
    #path("login",views.loginPage,name="loginPage"),
    path("register",views.register,name="register"),
    #path("logout",views.logout_view,name="mainlogout"),
    path("profile",views.profile,name="profile"),
    path("user_job_details",views.user_job,name="user_job_details"),
    path("nationality",views.nationality,name="nationality"),
    path("home_address_update",views.home_address_update,name="home_address_update"),
    #path("user_change",views.userchange,name="user_change"),
    path('password_change/', user_views.PasswordChangeView.as_view(template_name = 'user_password_change_form.html', 
        success_url = reverse_lazy('user_password_change_done')), name='user_password_change'),
    path('password_change/done/', user_views.PasswordChangeDoneView.as_view(template_name = 'user_password_change_done.html'), 
        name='user_password_change_done'),
    path('password_reset/', user_views.PasswordResetView.as_view(email_template_name='user_password_reset_email.html',
        template_name = 'user_password_reset_form.html', success_url = reverse_lazy('user_password_reset_done')), 
        name='user_password_reset'),
    path('password_reset/done/', user_views.PasswordResetDoneView.as_view(template_name='user_password_reset_done.html'),
        name='user_password_reset_done'),
    path('reset/<uidb64>/<token>/', user_views.PasswordResetConfirmView.as_view(template_name='user_password_reset_confirm.html',
        success_url = reverse_lazy('user_password_reset_complete')), 
        name='user_password_reset_confirm'),
    path('reset/done/', user_views.PasswordResetCompleteView.as_view(template_name='user_password_reset_complete.html'), 
        name='user_password_reset_complete'),    

]