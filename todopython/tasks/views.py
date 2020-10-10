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