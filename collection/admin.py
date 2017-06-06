from django.contrib import admin

# Register your models here.
from collection.models import Project # import model Project(thing in book)Chapter 6

#autimatic slug creation.  Chapter 6.
class ProjectAdmin(admin.ModelAdmin): #Changed ThingAdmin to ProjectAdmin
    model = Project #changed Thing to Project
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin) # register model.  Chapter 6  Added ProjectAdmin(ThingAdmin in the book)
