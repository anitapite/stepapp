from django.forms.fields import IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Step
from django.contrib.auth.decorators import login_required


# Create your views here.

class StepCount(forms.Form):
    monday_stepcount = forms.IntegerField(label="monday_stepcount")
    monday_activities = forms.CharField(label='monday_activities')
    tuesday_stepcount = forms.IntegerField(label="tuesday_stepcount")
    tuesday_activities = forms.CharField(label='tuesday_activities')
    wednesday_stepcount = forms.IntegerField(label="wednesday_stepcount")
    wednesday_activities = forms.CharField(label='wednesday_activities')
    thursday_stepcount = forms.IntegerField(label="thursday_stepcount")
    thursday_activities = forms.CharField(label='thursday_activities')
    friday_stepcount = forms.IntegerField(label="friday_stepcount")
    friday_activities = forms.CharField(label='friday_activities')
    saturday_stepcount = forms.IntegerField(label="saturday_stepcount")
    saturday_activities = forms.CharField(label='saturday_activities')
    sunday_stepcount = forms.IntegerField(label="sunday_stepcount")
    sunday_activities = forms.CharField(label='sunday_activities')
   

class DateInput(forms.DateInput):
    input_type = 'date'


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = [
            'monday_stepcount', 'monday_activities', 'monday_date', 
            'tuesday_stepcount', 'tuesday_activities', 'tuesday_date',
            'wednesday_stepcount', 'wednesday_activities', 'wednesday_date', 
            'thursday_stepcount', 'thursday_activities', 'thursday_date',
            'friday_stepcount', 'friday_activities', 'friday_date', 
            'saturday_stepcount', 'saturday_activities', 'saturday_date',
            'sunday_stepcount', 'sunday_activities', 'sunday_date',
            ]
        widgets = {
            'monday_date': DateInput(),
            'tuesday_date': DateInput(),
            'wednesday_date': DateInput(),
            'thursday_date': DateInput(),
            'friday_date': DateInput(),
            'saturday_date': DateInput(),
            'sunday_date': DateInput(),
        }


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

