from django import forms
from .models import *
from django.forms.models import inlineformset_factory

class ProblemForm(forms.ModelForm):

	class Meta:
		model = Problem
		exclude = ()


# ProblemFormSet = inflineformset_factory(Problem, Dataset, form=ProblemForm, fields=[''])
childFormset = inlineformset_factory(Problem, Dataset, form=ProblemForm, fields=('dataset', 'datasetDesc',), can_delete=False, extra=1)
