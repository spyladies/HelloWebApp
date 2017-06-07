from django.template.defaultfilters import slugify #added chapter 11
from django.shortcuts import render, redirect #added redirect in Chapter 9.
from collection.forms import ProjectForm  #changed Thing to Project.  Chapter 9.
from collection.models import Project #import project from collection.  Chapter 7.
from django.contrib.auth.decorators import login_required #import login_required.  Chapter 11
from django.http import Http404 #Chapter 11

# Create your views here.
def index(request): #defines index to return rendered index.html.  Chapter 4.
    number = 6 #defines a variable. Chapter 5
    thing = "Pyladies learning" #defines thing, I changed "Thing name" to pylady.  Chapter 5.
    projects = Project.objects.all() # defines projects, changed from things = Thing.objects.all(). Chapter 7

    return render(request, 'index.html', {'number': number,
    'thing': thing, 'projects': projects, #pass on thing.  Chapter 5.
    }) #Now also returns number and thing.  Chapter 5. Added projects: projects,

def project_detail(request, slug): #view added chapter 8, changed from thing_detail.
    project = Project.objects.get(slug=slug) #grabs the object.  Chapter 8.
    return render(request, 'projects/project_detail.html', {'project': project,}) #passes object to template.  Chapter 8.


# Added Chapter 9.
@login_required
def edit_project(request, slug): #changed thing to project
    # grab the object
    project = Project.objects.get(slug=slug)
       # make sure the logged in user is the owner of the project.  Change thing to project. Chapter 11.
    if project.user != request.user:
        raise Http404
    # set the form we're using
    form_class = ProjectForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=project) #changed thing to project
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('project_detail', slug=project.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=project)

    # and render the template.  thing to project.
    return render(request, 'projects/edit_project.html', {
        'project': project,
        'form': form,
    })
# Added chapter 11.  Renamed it create_project
def create_project(request):
    form_class = ProjectForm #changed Thing to Project

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            project = form.save(commit=False)

            # set the additional details
            project.user = request.user
            project.slug = slugify(project.name)

            # save the object
            project.save()

            # redirect to our newly created thing(project)
            return redirect('project_detail', slug=project.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'projects/create_project.html', {
        'form': form,
    })
