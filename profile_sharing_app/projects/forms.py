from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #featured_image for img upload
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']
        widgets = {
            # edit field class here for display in html page 
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        # provide specific class name here for the field
        # so that we can further work on css for each class
        # widget.attrs.update is the way to force to change the attribute
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        ### code above tries to acheive something like this:
        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})   # can also {'class': 'input', 'placeholder': 'This is default test in the box' }

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})
