from django import forms
from club.models import Project, Contactus

DEPARTMENT_CHOICES = (
        ('IT', 'IT'),
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('ME', 'ME'),
        ('EE', 'EE'),
        ('CE', 'CE')
    )

class ProjectForm(forms.ModelForm):
    """
    Idea Subimission Form Template
    """
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Your Idea Title',
        'style': 'color:black;',
    }))
    author = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Tell us your name',
        'style': 'color:black;',
    }))
    department = forms.CharField(label='Select your Department', widget=forms.Select(choices=DEPARTMENT_CHOICES, attrs={
        'class': 'form-control',
        'style': 'color:black;',
    }))
    pass_year = forms.IntegerField(initial=2020, required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-box',
        'size': 10,
        'placeholder': 'Describe your idea...',
        'style': 'color:black;',
    }), required=True)
    picture = forms.ImageField(required=False)

    views = forms.IntegerField(initial=0, widget=forms.HiddenInput())
    slug = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Project
        exclude = ('views', 'slug', 'publish', )


class ContactusForm(forms.ModelForm):
    """
    Contact us form template
    """

    name = forms.CharField(help_text="Enter your name", max_length=25, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Tell us your name'
    }))
    email = forms.EmailField(help_text="enter your mail", max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Email'
    }))
    subject = forms.CharField(help_text="Enter Subject", max_length=50, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(required=True, max_length=1000, widget=forms.TextInput(attrs={
        'class': 'form-control input-box',
        'placeholder': 'Write to us'
    }))

    class Meta:
        model = Contactus
        exclude = ('created',)
