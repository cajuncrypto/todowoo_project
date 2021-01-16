from django.urls import path
from . import views

urlpatterns = [
    path('todo/completed', views.TodoCompletedlist.as_view()),
]
