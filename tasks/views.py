from django.shortcuts import render

# Create your views here.
from django.conf.urls import url, include
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
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

class TaskView(View):
    success_url='..'
    model=Task
    fields=('text', 'complete')

class TaskAddView(TaskView, CreateView):
    pass

class TaskUpdateView(TaskView, UpdateView):
    pass
    
class TaskDetailView(TaskView, DetailView):
    pass

class TaskListView(TaskView, ListView):
    pass
    
class TaskDeleteView(TaskView, DeleteView):
    pass

urlpatterns = [
    url(r'^new', TaskAddView.as_view(), name='task_add'), # ADD(GET form)
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^edit', TaskUpdateView.as_view(), name='task_edit'), # EDIT(GET form)
        #url(r'^', TaskDetailView.as_view(), name='task_detail'), # READ, EDIT(POST form), DELETE?
        url(r'^kill', TaskDeleteView.as_view(), name='task_delete'),
    ])),
    url(r'^', TaskListView.as_view(), name='task_list'), # BROWSE, ADD(POST form)
]