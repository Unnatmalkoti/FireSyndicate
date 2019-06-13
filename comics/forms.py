from django import forms
from PIL import Image
from .models import Comic, Chapter
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ChapterCreateForm(forms.ModelForm):

	class Meta():
		model = Chapter
		fields= ["number", "name","comic"]
		# widgets = {"comic": forms.HiddenInput()}

class ChapterImagesForm(forms.Form):
	def __init__(self, *args, **kwargs):
		if kwargs.get("images"):
			self.images = kwargs.pop("images")

		super(ChapterImagesForm, self).__init__(*args, **kwargs)  # and carry on to init the form

	def clean(self):
		for image in self.images:
			try:
				im = Image.open(image)
				im.verify()
			except:
				raise forms.ValidationError(_("Upload valid images"))
		return self.cleaned_data

	images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))



class ComicCreateForm(forms.ModelForm):
	class Meta():
		model = Comic
		fields= ["title","author","artist", "description", "cover", "status"]

# class LoginForm(forms.Form):
# 	user_name   = forms.CharField(
# 		max_length= 20,
# 		widget=forms.TextInput(attrs={'class': "input-lg"}),
# 		label = "")
# 	password 	= forms.CharField(max_length= 30,label = "hi", widget = forms.PasswordInput())
