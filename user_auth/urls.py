from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for user_auth views
    path('signUp/', views.signUp, name='signUp'),
    path('logIn/', views.logIn, name='logIn'),
    # path('passwordRest/', views.passwordRest, name='passwordRest'),
    # path('logOut/', views.logOut, name='logOut'),
]
