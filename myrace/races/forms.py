from django import forms
from .models import Race

class SearchForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    search_txt = forms.CharField(label="", max_length=50)

