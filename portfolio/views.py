from django.shortcuts import render
from .models import Project , Contactus
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.core import validators
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request,'index.html' , {'projects':projects})



def about(request):
    return render(request,'about.html' )

def contact(request):
    return render(request,'contact.html' )


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        datas = Contactus(name = name, email = email, message = message)
        datas.save()
        return render(request, 'contact_us.html', {'names':datas})

    else:
        return HttpResponseRedirect(reverse('portfolio:contact'))




