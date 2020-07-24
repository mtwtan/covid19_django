from django import forms

class FilterByCountyForm(forms.Form):
  county = forms.ChoiceField(help_text="Select county to filter.")