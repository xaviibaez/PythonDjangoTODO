from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hola')

    # Vamos a devolver el list.html
    return render(request, 'tasks/list.html')