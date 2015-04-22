from django import forms
from django.contrib.auth.models import User
from rango.models import UserModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('website',)

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class UpdateUserProfileForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = ('website',)