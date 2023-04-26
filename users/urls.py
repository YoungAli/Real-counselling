from django.urls import path, include
from .views import login_user, logout_user, signup_user

urlpatterns = [
    path('login/', login_user, name='login'),
    path('signup/', signup_user, name='signup'),
    path('logout/', logout_user, name='logout')
]