from django.shortcuts import render
from .models import Project

def home(request):
    return render(request,'my/home.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'my/project_list.html', {'projects': projects})

def base(request):
    return render(request,'my/base.html')
def about(request):
    return render(request,'my/about.html')
def contact(request):
    return render(request,'my/contact.html')
def certificates(request):
    return render(request,'my/certificates.html')
def skills(request):
    return render(request,"my/skills.html")

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)

        return redirect('contact_success')  # ← redirect to success page

    return render(request, 'my/contact.html')


def contact_success(request):
    return render(request, 'my/success.html')




# views.py
from django.shortcuts import render

def portfolio(request):
    return render(request, 'my/portfolio.html')
