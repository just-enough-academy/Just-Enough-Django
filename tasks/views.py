from django.shortcuts import render

# Create your views here.
from django.conf.urls import url, include
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
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

class TaskView(generic.View):
    success_url='..'
    model=Task
    fields=('text', 'complete')

class TaskAddView(TaskView, generic.CreateView):
    success_url='.'

class TaskUpdateView(TaskView, generic.UpdateView):
    pass
    
class TaskDetailView(TaskView, generic.DetailView):
    pass

class TaskListView(TaskView, generic.ListView):
    COMPLETED='y'
    INCOMPLETE='n'
    COMPLETED_QS='complete'

    def get_completed_qs(self):
        return self.request.GET.get(self.COMPLETED_QS)

    def is_complete(self):
        completed = self.get_completed_qs()

        if completed in (self.COMPLETED, self.INCOMPLETE):
            return (True if completed is self.COMPLETED 
                else False)

    def get_context_data(self, **kwargs):
        ## FIXME: This don't work, but it's close...!
        return super().get_context_data(**kwargs) + {
            'COMPLETED': self.COMPLETED,
            'INCOMPLETE': self.INCOMPLETE,
            'QS': self.COMPLETED_QS
        }
        
    def get_queryset(self):
        
        tasks = super().get_queryset()
        
        if self.request.GET.get('complete') is self.INCOMPLETE: # ballot-x
            return tasks.filter(complete=False) 
            # show "incomplete" tasks

        if self.request.GET.get('complete') is self.COMPLETED: # ballot-check
            return tasks.filter(complete=True)
            # show "completed" tasks

        return tasks
        # show everything
    
class TaskDeleteView(TaskView, generic.DeleteView):
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