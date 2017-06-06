from django.shortcuts import render

# Create your views here.
def index(request): #defines index to return rendered index.html.  Chapter 4.
    number = 6 #defines a variable. Chapter 5
    thing = "Pyladies learning" #defines thing, I changed "Thing name" to pylady.  Chapter 5.
    return render(request, 'index.html', {'number': number,
    'thing': thing, #pass on thing.  Chapter 5.
    }) #Now also returns number and thing.  Chapter 5.
