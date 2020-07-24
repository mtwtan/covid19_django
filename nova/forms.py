from django import forms
from .models import Counties
from django.forms import ModelChoiceField
class FilterByCountyForm(forms.Form):
  county = forms.ModelChoiceField(queryset=Counties.objects.using('data').values_list('county'))
