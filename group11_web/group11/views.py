from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.forms import BaseModelFormSet, BaseFormSet, BaseInlineFormSet, Textarea, FileInput

from .models import Problem, Dataset
from django.forms.models import inlineformset_factory
from django.urls import reverse
# from .forms import *
from django.db import transaction
# Create your views here.

# def homePage(request):
# 	return HttpResponse('Hello, World!')

class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

class ProblemsView(ListView):
	template_name = 'problems.html'
	model = Problem
	context_object_name = 'problemsList'

# class RequiredFormSet(BaseFormSet):
#     # def clean(self):
#     #     super().clean()
#     def __init__(self, *args, **kwargs):
#         super(RequiredFormSet, self).__init__(*args, **kwargs)
#         for form in self.forms:
#             form.empty_permitted = False

class TestFormSet(BaseInlineFormSet):
	def clean(self):
		super().clean()
		# for form in self.forms:
		# 	form.empty_permitted = False
		if any(self.errors):
			return
		if not self.forms[0].has_changed():
			raise forms.ValidationError('Please add at least one vehicle.')
	# def __init__(self, *args, **kwargs):
	# 	super(TestFormSet, self).__init__(*args, **kwargs)
	# 	for form in self.forms:
	# 		form.empty_permitted = False

childFormset = inlineformset_factory(Problem, Dataset, fields=('dataset', 'datasetDesc',), can_delete=False, extra=1, 
	formset=TestFormSet, widgets={'datasetDesc': Textarea(attrs={'required': True}), 'dataset': FileInput(attrs={'required': True})})

class CreateProblemView(CreateView):
	model = Problem
	template_name = 'new_problem.html'
	fields = ['title', 'problemInfo', 'evaluationCode',]

	# def clean(self):
	# 	super().clean()
	# 	for form in self.forms:
	# 		form.empty_permitted = False

	# def __init__(self, *args, **kwargs):
	# 	super(CreateProblemView, self).__init__(*args, **kwargs)
	# 	for form in self.forms:
	# 		form.empty_permitted = False

	def get_context_data(self, **kwargs):
		# context = super(DataSetView, self).get_context_data(**kwargs)
		data = super(CreateProblemView, self).get_context_data(**kwargs)
		if self.request.POST:
			data['datasets'] = childFormset(self.request.POST, self.request.FILES, instance=self.object)
		else:
			data['datasets'] = childFormset(instance=self.object)
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		datasets = context["datasets"]
		self.object = form.save()
		if datasets.is_valid():
			datasets.instance = self.object
			datasets.save()
			# print(datasets["datasetDesc"])
			print(datasets.request.datasetDesc)
		# if not datasets.is_valid():
		# 	raise ValidationError('Invalid file extension.')
		return super(CreateProblemView, self).form_valid(form)

	# def form_valid(self, form):
	# 	context = self.get_context_data()
	# 	datasets = context['datasets']
	# 	with transaction.atomic():
	# 		self.object = form.save()
	# 		if datasets.is_valid():
	# 			datasets.instance = self.object
	# 			datasets.save()
	# 	return super(CreateProblemView, self).form_valid(form)

	def get_success_url(self):
		return reverse('problem_detail', kwargs={'pk': self.object.pk})
		# return reverse("problems:list")

	# def form_valid(self, form):
	# 	form.instance.
	# def get_context_data(self, **kwargs):
	# 	kwargs['dataset'] = Dataset.objects.get(pk=self.kwargs['pk'])
	# 	return super().get_context_data(**kwargs)

		#form_valid(form)

# class DataSetView(CreateView):
# 	model = Dataset
# 	fields = ['dataset', 'datasetDesc']
# 	template_name = 'new_problem.html'

class ProblemDetailView(DetailView):
	model = Problem
	template_name = 'problem_detail.html'

# def probDetail(request, problemID):
# 	problem = get_object_or_404(Problems, pk=problemID)
# 	return render(request, 'problem_detail.html', {'problem': problem})