from django.shortcuts import render,redirect
from .models import todo

# Create your views here.
def home(request):
    data = todo.objects.all()
    return render(request, 'home.html', {'data': data})

def add(request):
    tododata = request.POST['todo']
    todo_item = todo(content=tododata)
    todo_item.save()
    return redirect(home)