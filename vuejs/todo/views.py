from django.shortcuts import render
from django.views.decorators.http import require_POST

from todo.models import Todo
from django.http import JsonResponse


def todo_fetch(request):
    todos = Todo.objects.all()
    todo_list = []
    for index, todo in enumerate(todos, start=1):
        todo_list.append({'id': index, 'title': todo.title, 'completed': todo.completed})

    return JsonResponse(todo_list, safe=False)


import json
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm


@csrf_exempt
@require_POST
def todo_save(requset):
    if requset.body:
        data = json.loads(requset.body)
        if 'todos' in data:
            todos = data['todos']
            Todo.objects.all().delete()
            for todo in todos:
                print('todo', todo)
                form = TodoForm(todo)
                if form.is_valid():
                    form.save()
    return JsonResponse({})

def index(request):
    return render(request, 'todo/list.html')
