from django import forms
from django.contrib.auth.models import User
from rango.models import UserModel, ContentModel, Audio

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('website','picture')

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class UpdateUserProfileForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = ('website','picture')

class UploadContentForm(forms.ModelForm):
    class Meta:
        model = ContentModel
        fields = ('title', 'artist', 'genre', 'description', 'album', 'website')

class UploadMusicForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('mediaFile',)