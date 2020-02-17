from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	# model = CustomUser
	# # fields = UserCreationForm.Meta.fields + ('age',)
	Class Meta(UserCreationForm.Meta):
		models = CustomUser
		fields = ('username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		# fields = UserChangeForm.Meta.fields
		fields = ('username', 'email', 'age',)

