from django import forms
from .models import Counties
from django.forms import ModelChoiceField
class FilterByCountyForm(forms.Form):
  county = forms.ModelChoiceField(queryset=Counties.objects.using('data').all(),values_list('county'))
