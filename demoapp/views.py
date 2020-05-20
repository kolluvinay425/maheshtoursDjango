from django.shortcuts import render
from django.template import loader
from .models import Tour

# Create your views here.
def home(request):
    
    return render(request,'demoapp/home.html')


def detail(request,tour_id):

    tour= Tour.objects.get(pk=tour_id)
    return render(request,'demoapp/detail.html',{'tour':tour})

def contact(request):
    return render(request,'demoapp/about.html')

def tour_package(request):
    tours = Tour.objects.all()

    return render(request,'demoapp/tours.html',{'tours':tours})



