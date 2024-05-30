from django.shortcuts import render, redirect

from app.models import Todo


# Create your views here.


def todo_list(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request,'index.html',{'todos':todos})



def create_todo(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        Todo.objects.create(title=title,description=description)
    return redirect('index')


def complete_todo(request,pk):
    todo=Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    return redirect('index')


def delete_todo(request,pk):
    todo=Todo.objects.get(pk=pk)
    todo.delete()
    todo.save()
    return redirect('index')
