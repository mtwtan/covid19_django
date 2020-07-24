from django import forms
from .models import Counties
from django.forms import ModelChoiceField
class FilterByCountyForm(forms.Form):
  county = forms.ModelChoiceField(queryset=Counties.objects.using('data').all().only('county'),empty_label="Select County",to_field_name="county",label_from_instance="county",help_text="Select county to filter.")
