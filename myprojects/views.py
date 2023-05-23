#from django.http import HttpResponseRedirect

from unicodedata import name
from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from  django.contrib.auth.decorators import  login_required
from django.core.mail import send_mail


# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('project_index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Un compte a ete cree pour' + user)
                return redirect('login')
        context = {
            'form':form
        }
        return render(request, 'registration/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('project_index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user =  authenticate(request, username =username, password=password)

            if user is not None:
                login(request, user)
                return redirect('project_index')
            else:
                messages.info(request, 'username or password incorect')
            
        context = {}
        return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    
def home(request):
    return render(request, 'home.html')

def project_index(request):
    projects = Project.objects.all()
    #services = Service.objects.all()
    context= {
        'projects': projects,
        #'services': services
    }
    return render(request, 'project_index.html', context)

@login_required(login_url='login')  
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

@login_required(login_url='login')  
def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    context = {
        'service': service
    }
    return render(request, 'service_detail.html', context)

@login_required(login_url='login') 
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name'),
        email = request.POST.get('email'),
        subject = request.POST.get('subject'),
        message = request.POST.get('message'),

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message : {}

        From : {}
        '''.format(data['message'], data['email'])
        
        send_mail(data['subject'], message, '', ['foulaly2018@gmail.com'])
        messages.success(request, 'Thank you')
        return redirect('/myprojects/')
    return render(request, 'contact.html', {})

def blog(request):
    return render(request, '../blog/blog.html')
    
@login_required(login_url='login') 
def about(request):
    return render(request, 'aboutus.html')