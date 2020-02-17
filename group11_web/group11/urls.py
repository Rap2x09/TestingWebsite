from django.urls import path
from .views import HomePageView, AboutPageView, ProblemsView, CreateProblemView, ProblemDetailView


urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'),
	path('problems/', ProblemsView.as_view(), name='problems'),
	path('problems/new/', CreateProblemView.as_view(), name='new_problem'),
	path('problems/<int:pk>/', ProblemDetailView.as_view(), name='problem_detail'),
	# path('problems/<int:pk>/', probDetail, name='problem_detail'),

    #path('', homePage, name='home')
]
