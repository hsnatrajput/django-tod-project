from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todo(title=title, description=description)
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_create.html')

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_update.html', {'todo': todo})

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo_list')
