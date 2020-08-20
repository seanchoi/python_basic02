from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the result</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<h1> Current Date and Time: </h1>" + str(dt)
    return HttpResponse(s)