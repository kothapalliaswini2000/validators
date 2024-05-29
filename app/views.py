from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse(str(TFDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render (request,'insert_topic.html',d)


def insert_Webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            na=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']
            #WO=Webpage.objects.get_or_create(topic_name=tn,name=na,url=url,email=email)[0]
            #WO.save()
            return HttpResponse(str(WFDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render (request,'insert_Webpage.html',d)


def insert_AccessRecord(request):
    EAFO=WebpageForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            name=AFDO.cleaned_data['name']
            
            date=AFDO.cleaned_data['date']
            author=AFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=name,date=date,author=author)[0]
            AO.save()
            return HttpResponse('Data is submitted')
        else:
            return HttpResponse('Invalid data')
    return render (request,'insert_AccessRecord.html',d)




    
