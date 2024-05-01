from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    # path('signUp/', views.signUp, name='signUp'),
    # path('logIn/', views.logIn, name='logIn'),
    path('viewPasswords/', views.viewPasswords, name='viewPasswords'),
    path('settings/', views.settings, name='settings'),
]
