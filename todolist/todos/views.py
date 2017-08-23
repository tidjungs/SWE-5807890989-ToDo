from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
  todos = Todo.objects.all()
  return render(request, 'index.html', { 'todos': todos })

def details(request, id):
  todo = Todo.objects.get(id=id)
  return render(request, 'details.html', { 'todo': todo })

def add(request):
  if(request.method == 'POST'):
    title = request.POST['title']
    text = request.POST['text']
    
    todo = Todo(title=title, text=text)
    todo.save()

    return redirect('/todos')
  else:
    return render(request, 'add.html')