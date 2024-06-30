from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('todo')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',
        {'all_items': all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'] )
    new_item.save()
    return HttpResponseRedirect ('/todo/')
           
def deleteTodo(request, todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect ('/todo/') 

