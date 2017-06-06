from django.shortcuts import render
from collection.models import Project #import project from collection.  Chapter 7.

# Create your views here.
def index(request): #defines index to return rendered index.html.  Chapter 4.
    number = 6 #defines a variable. Chapter 5
    thing = "Pyladies learning" #defines thing, I changed "Thing name" to pylady.  Chapter 5.
    projects = Project.objects.all() # defines projects, changed from things = Thing.objects.all(). Chapter 7

    return render(request, 'index.html', {'number': number,
    'thing': thing, 'projects': projects, #pass on thing.  Chapter 5.
    }) #Now also returns number and thing.  Chapter 5. Added projects: projects,
