from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'name' : 'Pronay', 'age' : '23', 'lst': ['Python','is','best'], 'birthday' : datetime.datetime.now(), 'val': ''}
    return render(request, "home.html", d)