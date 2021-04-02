from django.forms.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

class StepCount(forms.Form):
    stepcount = forms.IntegerField(label="Stepcount")
    activities = forms.CharField(label='Activities')

def index(request):
    return render(request, 'steps/index.html')

def add(request):
    return render(request, 'steps/add.html', {
        'form': StepCount()
    })