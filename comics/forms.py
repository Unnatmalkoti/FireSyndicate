from django import forms
from .models import Comic, Chapter

class ChapterCreateForm(forms.ModelForm):

	class Meta():
		model = Chapter
		fields= ["number", "name","comic"]
		widgets = {"comic": forms.HiddenInput()}

class ChapterImagesForm(forms.Form):
	images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ComicCreateForm(forms.ModelForm):
	class Meta():
		model = Comic
		fields= ["title", "description", "cover", "status"]

class LoginForm(forms.Form):
	user_name   = forms.CharField(max_length= 20)
	password 	= forms.CharField(max_length= 30, widget = forms.PasswordInput())

