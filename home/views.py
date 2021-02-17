from django.shortcuts import render, HttpResponse
from home import models
from home.models import Person

def home(request):
    # return HttpResponse("This is My Home Page (/)")
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        person = Person()
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        person.name = name
        person.email = email
        person.desc = desc

        person.save()
        print("done")
    return render(request, 'contact.html')


def projects(request):
    # return HttpResponse("This is My Projects Page (/)")
    return render(request, 'projects.html')


def about(request):
    # return HttpResponse("This is My About Page (/)")

    return render(request, 'about.html')
