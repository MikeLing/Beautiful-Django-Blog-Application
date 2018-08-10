from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'webapp/index.html')

def contact(request):
    return render(request, 'webapp/basic.html',{'content':['If you would like to contact me, please email me.','Bharatkaistha@gmail.com']})
