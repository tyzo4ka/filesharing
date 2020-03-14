from django import forms
from webapp.models import File


class FileSearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Find')


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'caption', 'access']


class AnonFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'caption']
