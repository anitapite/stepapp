from django.forms.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Step

# Create your views here.

class StepCount(forms.Form):
    stepcount = forms.IntegerField(label="Stepcount")
    activities = forms.CharField(label='Activities')

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['stepcount', 'activities']

def index(request):
    return render(request, 'steps/index.html')

def add(request):
    form = StepForm(request.POST)
    if form.is_valid():
        form.save()
        form = StepForm()
    return render(request, 'steps/add.html', {
       'form': form
   })

def history(request):
    return render(request, 'steps/history.html')

def hunindex(request):
    return render(request, 'steps/hunindex.html')