from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    # return HttpResponse('Hola')

    # renderizamos las tasks con sus atributos
    tasks = Task.objects.all()
    
    form = TaskForm()

    #iteramos
    context = {'tasks':tasks, 'form':form}

    # Vamos a devolver el list.html
    return render(request, 'tasks/list.html', context)