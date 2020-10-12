from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    # return HttpResponse('Hola')

    # renderizamos las tasks con sus atributos
    tasks = Task.objects.all()
    
    form = TaskForm()

    # Despues de hacer el POST volvera a esta view
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # Si es valido, guardamos el form en la BBDD
        if form.is_valid():
            form.save()

        # hacemos return de la misma template -> redirect
        return redirect('/')

    # iteramos
    context = {'tasks':tasks, 'form':form}

    # Vamos a devolver el list.html
    return render(request, 'tasks/list.html', context)

# Update task, pk -> primary key
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    context = {'form':form}

    # Despues de hacer el POST volvera a esta view
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        # Si es valido, guardamos el form en la BBDD
        if form.is_valid():
            form.save()

        # hacemos return a '/'
        return redirect('/')

    return render(request, 'tasks/update_task.html', context)

# Delete task, pk -> primary key
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        # hacemos return a '/'
        return redirect('/')

    context = {'item':item}

    return render(request, 'tasks/delete_task.html', context)