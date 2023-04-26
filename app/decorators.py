from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def for_admins(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    A decorator to check logged in user is an admin and redirects to the login page if the user isn't authenticated.
    '''
    actual_decorator = user_passes_test(
        lambda user: user.is_active and user.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
