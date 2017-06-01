from django.shortcuts import render

# Create your views here.
def index(request): #defines index to return rendered index.html.  Chapter 4.
    # this is your new view
    return render(request, 'index.html')
