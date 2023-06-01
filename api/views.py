from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def hello(request):
    return HttpResponse('Hello, World!')

def user_list(request):
    users = User.objects.all()
    return render(request, 'userlist.html', {'users': users})

def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user_details.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        user = User(name=name, email=email, role=role)
        user.save()
        return redirect('user_list')
    return render(request, 'user_create.html')
