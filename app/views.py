from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def djforms(request):
    ESTFO=studentform()
    d={'ESTFO':ESTFO}

    if request.method=='POST':
        SFDO=studentform(request.POST)
        print(SFDO)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid Data') 

    return render(request,'djforms.html',d)
