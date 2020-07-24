from django import forms
from .models import Counties
from django.forms import ModelChoiceField

COUNTY =( 
    ("Arlington", "Arlington"), 
    ("District of Columbia", "District of Columbia"), 
    ("Fairfax", "Fairfax"), 
    ("Montgomery", "Montgomery"),
) 

class FilterByCountyForm(forms.Form):
  #county = forms.ModelChoiceField(queryset=Counties.objects.using('data').values_list('county'))
  county = forms.ChoiceField(choices = COUNTY)  