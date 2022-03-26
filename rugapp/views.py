from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):



    return render(request, 'rugapp/home.html')
def searched(request):


    return render(request, 'rugapp/searched.html')
def about(request):



    return render(request, 'rugapp/about.html')
def report(request):



    return render(request, 'rugapp/report.html')