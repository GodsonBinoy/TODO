from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

class Tasklistview(ListView):

    model = Task
    template_name = 'index.html'
    context_object_name = 'view'


class Detailview(DetailView):

    model = Task
    template_name = 'detail.html'
    context_object_name = 'c'


class Editview(UpdateView):

    model = Task
    template_name = 'update.html'
    context_object_name = 'edit'

# Create your views here.
def add(request):
    view=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request, 'index.html',{'view':view})

def delete(request,id):
    tasks= Task.objects.get(id=id)
    if request.method=='POST':
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    abc=Task.objects.get(id=id)
    form=TaskForm(request.POST or None ,instance=abc)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'abc':abc})
