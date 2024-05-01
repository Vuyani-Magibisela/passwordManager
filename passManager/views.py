from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "landing.html")

def viewPasswords(request):
    return render(request, 'view_passwords.html')

def about(request):
    return render(request, 'about.html')

def settings(request):
    return render(request, 'settings.html')

