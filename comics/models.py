from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
    
import os, random

# Create your models here.

class Comic(models.Model):
	title 			= models.CharField(max_length = 120)
	author			= models.CharField(max_length = 120)
	artist			= models.CharField(max_length = 120)
	description		= models.TextField()
	cover 			= models.ImageField(upload_to="")
	status			= models.PositiveSmallIntegerField(default = True)				 # 1 = Working,		2 = on Hold,	0 = Dropped , hidden = 4
	views_cnt		= models.PositiveIntegerField(default = 0)

	def __str__(self):
		return "{title}".format(title = self.title)

	def get_absolute_url(self):
		return reverse("comic-detail", kwargs = {'pk' : self.pk}) 

	def delete(self, *args, **kwargs):
		self.cover.delete()
		super().delete(*args, **kwargs)

	ordering	=	["title"]


class Chapter(models.Model):
	number 			= models.DecimalField(max_digits = 10,  decimal_places = 2)
	name			= models.CharField(max_length = 120, blank = True, null = True)
	views_cnt		= models.PositiveIntegerField(default = 0, null = False)
	updated_at 		= models.DateTimeField(auto_now_add=True)
	created_at 		= models.DateTimeField(auto_now=True)
	comic 			= models.ForeignKey(Comic,on_delete=models.CASCADE)

	def __str__(self):
		return "Chapter {num} | {comic}".format(num= self.number, comic = self.comic)

	def get_absolute_url(self):
		return reverse("chapter-view", kwargs = {'pk' : self.pk}) 



	ordering = ['-number']



class Page(models.Model):

	chapter			= models.ForeignKey(Chapter, on_delete= models.CASCADE)
	image 			= models.ImageField(upload_to ="" )
	page_number		= models.PositiveIntegerField()
	updated_at		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{id}'.format(id =self.id)

@receiver(post_delete, sender=Page)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

@receiver(post_delete, sender=Comic)
def submission_delete(sender, instance, **kwargs):
    instance.cover.delete(False) 