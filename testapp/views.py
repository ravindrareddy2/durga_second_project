from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse
def datetime_view(request):
    date = datetime.datetime.now()
    s = "<h1>Current time is </h1>" +"<h1>"+str(date)+"</h1>"
    return HttpResponse(s)