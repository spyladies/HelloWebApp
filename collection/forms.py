#added chapter 9.
from django.forms import ModelForm #import from django #chapter 9
from collection.models import Project #import project model #chapter 9
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description',)
