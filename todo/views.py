from django.shortcuts import render,redirect
from .models import todo

# Create your views here.

#home view
def home(request):
    data = todo.objects.all()
    return render(request, 'home.html', {'data': data})

def add(request):
    tododata = request.POST['todo']
    todo_item = todo(content=tododata)
    todo_item.save()
    return redirect(home)

def deleteItem(request, todo_id):
    item = todo.objects.get(id=todo_id)
    item.delete()
    return redirect(home)