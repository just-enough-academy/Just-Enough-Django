from django.shortcuts import render

# Create your views here.
from django.conf.urls import url, include
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task

def hello_world(request):
    return HttpResponse('Hello, World!')

def task_list(request):
    return render(request, 'task_list.html', { 
        'tasks': Task.objects.all() 
    })

def task_detail(request, task_id):
    return render(request, 'task_detail.html', { 
        'task': Task.objects.get(pk=task_id) 
    })

urlpatterns = [
    url(r'^new', hello_world), # ADD(GET form)
    url(r'^(?P<task_id>[0-9]+)', include([
        url(r'^', task_detail), # READ, EDIT(POST form), DELETE?
        url(r'^edit', hello_world) # EDIT(GET form)
    ])),
    url(r'^', ListView.as_view(model=Task), name='task_list'), # BROWSE, ADD(POST form)
]