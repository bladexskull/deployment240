from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from apptwo.models import User
from . import models
from . import forms

def formcall(request):
    formtag=forms.UserForm()
    modobj = models.User()



    if request.method=='POST':
        formtag=forms.UserForm(request.POST)
        if formtag.is_valid():
            formtag.save()
            return help(request)


    return render(request,'apptwo/formmodel.html', {'formtag':formtag})

def help(request):
    iteratelist = User.objects.order_by('firstname')
    my_dict = {'temptag':iteratelist }
    return render(request,'apptwo/help.html',context=my_dict)

def new(request):
    mydict={ 'key':"test for filters"}
    return render(request,'apptwo/new.html',context=mydict)

def index(request):
    iteratelista = User.objects.order_by('lastname')
    mydict = {'template_tag':iteratelista }
    return render(request,'apptwo/index.html',context=mydict)
