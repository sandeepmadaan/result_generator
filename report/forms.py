
from django import forms
from django.forms import ModelChoiceField
from result_generator.report.models import *

class SelectType(forms.Form):
	std = forms.ModelChoiceField(queryset=Class.objects.all()) 
	test = forms.ModelChoiceField(queryset=Tests,objects.all()) 

