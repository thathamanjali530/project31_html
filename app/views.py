from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TEFO=TopicForm()
    d={'TEFO':TEFO}
    if request.method=='POST':
        TDFO=TopicForm(request.POST)
        if TDFO.is_valid():
            TDFO.save()
            return HttpResponse('topic data inserted')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WEFO=WebpageForm()
    d={'WEFO':WEFO}
    if request.method=='POST':
        WDFO=WebpageForm(request.POST)
        if WDFO.is_valid():
            WDFO.save()
            return HttpResponse('topic data inserted')

    return render(request,'insert_webpage.html',d)