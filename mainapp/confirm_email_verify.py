from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.core.mail import BadHeaderError, send_mail
from binascii import Error as BASE64ERROR
from django.contrib.auth import get_user_model
from django.utils import timezone
from loginpgm.models import AddressHistory
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from smtplib import SMTPException

from django.conf import settings


class GetFieldFromSettings:
    """
    This class fetches the attributes that are defined in settings.py of your project by user OR Django itself.
    self.default_configs : is a dict with keys as the names used in this app and values being a tuple of 
                           attributes defined in settings.py and their corresponding default values if not found.
    
    There is a special case in "get" method, if you set "VERIFICATION_SUCCESS_TEMPLATE" as None is settings.py, it 
    will skip the intermidiate page where success information is displayed. (This is better explained in docs.)

    The "get" method takes the name of the attributes as input, checks for it in settings.py, 
            if found:
                returns the corresponding value.
            else:
                returns the default value from "self.defaults_configs".
    """

    def __init__(self):

        self.defaults_configs = {
            'debug_settings': (
                'DEBUG', 
                False
            ),

            'subject': (
                "SUBJECT", 
                "Email Verification Mail"
            ),

            'email_field_name': (
                "EMAIL_FIELD_NAME", 
                "email",
            ),

            'html_message_template': (
                "HTML_MESSAGE_TEMPLATE", 
                'email_verification_msg.html'
            ),

            'from_alias': (
                "DEFAULT_FROM_EMAIL", 
                'noreply<noreply@gmail.com>',
            ),

            'verification_success_redirect': (
                'LOGIN_URL',
                'accounts_login'
            ),

            'verification_success_template': (
                'VERIFICATION_SUCCESS_TEMPLATE',
                'email_verification_successful.html'
            ),

            'verification_success_msg': (
                'VERIFICATION_SUCCESS_MSG',
                "Your Email is verified successfully and account has been activated. You can login with the credentials now..."
            ),

            'verification_failed_template': (
                'VERIFICATION_FAILED_TEMPLATE',
                'email_verification_failed.html'
            ),

            'verification_failed_msg': (
                'VERIFICATION_FAILED_MSG',
                "There is something wrong with this link, can't verify the user..."
            ),
        }

    def get(self, field_name, raise_exception=True, default_type=str):
        attr = getattr(
            settings, 
            self.defaults_configs[field_name][0],  # get field from settings
            self.defaults_configs[field_name][1]   # get default value if field not defined
        )
        if (attr == '' or attr is None or not isinstance(field_name, default_type)) and raise_exception:
            if field_name == 'verification_success_template' and attr is None:
                return None
            raise AttributeError
        return attr

class _UserActivationProcess:
    """
    This class is pretty self.explanatory...
    """

    def __init__(self):
        pass

    def __activate_user(self, user):
        user.is_active = True
        user.last_login = timezone.now()
        user.save()


    def verify_token(self, useremail, usertoken):
        try:
            email = urlsafe_b64decode(useremail).decode('utf-8')
            token = urlsafe_b64decode(usertoken).decode('utf-8')
        except BASE64ERROR:
            return False

        inactive_users = get_user_model().objects.filter(email=email)
        try:
            if inactive_users:
                for unique_user in inactive_users:
                    valid = default_token_generator.check_token(unique_user, token)
                    if valid:
                        self.__activate_user(unique_user)
                        return valid
                return False
            return False
        except:
            return False


def _verify_user(useremail, usertoken):
    return _UserActivationProcess().verify_token(useremail, usertoken)


success_redirect = GetFieldFromSettings().get('verification_success_redirect')

success_msg = GetFieldFromSettings().get('verification_success_msg')
failed_msg = GetFieldFromSettings().get('verification_failed_msg')

failed_template = GetFieldFromSettings().get('verification_failed_template')
success_template = GetFieldFromSettings().get('verification_success_template')


def verify_user_and_activate(request, useremail, usertoken):
    """
    A view function already implemented for you so you don't have to implement any function for verification
    as this function will be automatically be called when user clicks on verification link.

    verify the user's email and token and redirect'em accordingly.
    """

    if _verify_user(useremail, usertoken):
        if success_redirect and not success_template:
            messages.success(request, success_msg)
            return redirect(to=success_redirect)
        return render(
            request,
            template_name=success_template,
            context={
                'msg': success_msg,
                'status': 'Verification Successful!',
                'link': reverse(success_redirect)
            }
        )
    else:
        return render(
            request,
            template_name=failed_template,
            context={
                'msg': failed_msg,
                'status': 'Verification Failed!',
            }
        )


class _VerifyEmail:
    """
    This class does four things:
    1. creates tokens for each user.
    2. set each user as inactive and saves it
    3. embed encoded token with encoded email to make verification link.
    4. sends the email to user with that link.
    """

    def __init__(self):
        self.settings = GetFieldFromSettings()

    def __get_hashed_token(self, user):
        return urlsafe_b64encode(str(default_token_generator.make_token(user)).encode('utf-8')).decode('utf-8')

    def __make_verification_url(self, request, inactive_user, useremail):
        token = self.__get_hashed_token(inactive_user)
        email_enc = urlsafe_b64encode(str(useremail).encode('utf-8')).decode('utf-8')
        link = f"/verification/user/verify-email/{email_enc}/{token}/"
        
        absolute_link = request.build_absolute_uri(link)
        
        return absolute_link

    def send_verification_link(self, request, form):
        inactive_user = form.save(commit=False)
        #home_address = request.POST['home_address']
        #home_address_move_date = request.POST['home_address_move_date']
        #addresshistory = inactive_user
        inactive_user.is_active = False
        inactive_user.save()
        #address_instance = AddressHistory(home_address=home_address, home_address_move_date=home_address_move_date,
         #                                   addresshistory=addresshistory)
        #address_instance.save()
        
        
        
        try:
            useremail = form.cleaned_data.get(self.settings.get('email_field_name'))
            if not useremail:
                raise KeyError(
                    'No key named "email" in your form. Your field should be named as email in form OR set a variable'
                    ' "EMAIL_FIELD_NAME" with the name of current field in settings.py if you want to use current name '
                    'as email field.'
                )

            verification_url = self.__make_verification_url(request, inactive_user, useremail)
            subject = self.settings.get('subject')
            msg = render_to_string(self.settings.get('html_message_template', raise_exception=True),
                                   {"link": verification_url})

            try:
                send_mail(subject, strip_tags(msg), from_email=self.settings.get('from_alias'),
                          recipient_list=[useremail], html_message=msg)
                return inactive_user
            except (BadHeaderError, SMTPException):
                inactive_user.delete()
                return False

        except Exception as error:

            inactive_user.delete()
            if self.settings.get('debug_settings'):
                raise Exception(error)


#  These is supposed to be called outside of this module
def send_verification_email(request, form):
    return _VerifyEmail().send_verification_link(request, form)

