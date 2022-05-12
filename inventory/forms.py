from django import forms
from .models import *


class MaterialConfigurationForm(forms.ModelForm):
    class Meta:
        model = MaterialConfiguration
        fields = '__all__'


class MaterialForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Material.objects.all())

    class Meta:
        model = Material
        fields = '__all__'

    '''def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance')'''
