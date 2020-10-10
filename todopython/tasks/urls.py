from django.urls import path
from . import views

#URL routing
urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task")
]