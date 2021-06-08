from django.forms.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Step
from django.contrib.auth.decorators import login_required

# Create your views here.

class StepCount(forms.Form):
    stepcount = forms.IntegerField(label="Stepcount")
    activities = forms.CharField(label='Activities')

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['stepcount', 'activities']

@login_required
def index(request):
    return render(request, 'steps/index.html')

@login_required
def add(request):
    form = StepForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = StepForm()
    return render(request, 'steps/add.html', {
       'form': form
   })


def history(request):
    return render(request, 'steps/history.html')

@login_required
def hunindex(request):
    return render(request, 'steps/hunindex.html')

