from django.shortcuts import render

# Create your views here.
from django.conf.urls import url, include
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Task

def hello_world(request):
    return HttpResponse('Hello, World!')

def list_tasks(request):
    return HttpResponse(serialize('json', Task.objects.all()), 
        content_type='application/json')

urlpatterns = [
    url(r'^', list_tasks), # BROWSE, ADD(POST form)
    url(r'^new', hello_world), # ADD(GET form)
    url(r'^(?P<id>[0-9]+)', include([
        url(r'^', hello_world), # READ, EDIT(POST form), DELETE?
        url(r'^edit', hello_world) # EDIT(GET form)
    ]))
]