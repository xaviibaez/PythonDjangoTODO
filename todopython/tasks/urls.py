from django.urls import path
from . import views

#URL routing
urlpatterns = [
    path('', views.index)
]