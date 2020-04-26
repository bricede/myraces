from django import forms
from .models import Race

class SearchForm(forms.Form):
    search_txt = forms.CharField(label="", max_length=50)

