from django import forms
from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(label='query', max_length=100, widget=forms.TextInput(attrs={'class': "form-inline form-control mr-sm-2"}))