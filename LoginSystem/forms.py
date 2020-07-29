from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

TYPES = [
    ('MA', 'Manager'),
    ('PC', 'PCHO'),
    ('AP', 'Appliances'),
    ('HT', 'Home Theater'),
    ('MO', 'Mobile'),
    ('CH', 'Connected Home'),
    ('FL', 'Front Lanes'),
]

class SignUpForm(UserCreationForm):
	numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
	username = forms.CharField(max_length=7, validators=[numeric], label= 'Username', required = True)
	full_name = forms.CharField(max_length=100,label= 'Full Name', required = True)
	employee_type = forms.CharField(label = 'Employee Type', widget = forms.Select(choices = TYPES))

	class Meta:
		model = User
		fields = (
			'username',
			'password1',
			'password2',
			'employee_type',
			)

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.full_name = self.cleaned_data['full_name']
		user.employee_type = self.cleaned_data['employee_type']

		if commit:
			user.save()

		return user

