from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def index(request):
  todos = Todo.objects.all()
  return render(request, 'index.html', { 'todos': todos })

def details(request, id):
  todo = Todo.objects.get(id=id)
  return render(request, 'details.html', { 'todo': todo })