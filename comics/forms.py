from django import forms
import zipfile 
from io import BytesIO
from PIL import Image
from .models import Comic, Chapter
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ChapterCreateForm(forms.ModelForm):

	class Meta():
		model = Chapter
		fields= ["number", "name","comic"]

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

class ChapterZipForm(forms.Form):
	zip = forms.FileField()

	def is_valid(self):
		valid = super(ChapterZipForm, self).is_valid()
		if not valid :
			return valid

		try:  
			zip_file = zipfile.ZipFile(self.cleaned_data['zip'])

			for name in zip_file.namelist():
				data = zip_file.read(name)
				try:
					from PIL import Image
					image = Image.open(BytesIO(data))
					image.load()
					image = Image.open(BytesIO(data))
					image.verify()
				except:
					valid = False
					raise forms.ValidationError(_("Zip should have only images"))
			return True
		except :
			raise forms.ValidationError(_("Upload valid Zip file"))
		

class ComicCreateForm(forms.ModelForm):
	class Meta():
		model = Comic
		fields= ["title","author","artist", "description", "cover", "status"]
