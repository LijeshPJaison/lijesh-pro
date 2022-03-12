from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('haii')

def index2(request):
    return render(request,'temp.html')
def index3(request):
    return render(request,'example.html')

