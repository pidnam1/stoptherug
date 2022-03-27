from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from captcha.fields import CaptchaField

class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_style = 'inline'
    query = forms.CharField(label='query', max_length=100, widget=forms.TextInput(attrs={'class': "form-inline form-control mr-sm-2", 'placeholder':'Search'}))

class VoteForm(forms.ModelForm):

    vote = forms.IntegerField(max_value=100, min_value=0, label="Credibility Rating")
    comment = forms.CharField(max_length=5000, required=True, label="Comment", widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    captcha = CaptchaField()
    class Meta:
        model = NFTProject
        fields = ('vote', 'comment')

