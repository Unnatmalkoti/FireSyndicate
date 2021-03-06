from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django_cleanup.signals import cleanup_pre_delete, cleanup_post_delete
    
import os, random

# Create your models here.


class Tag(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField( auto_now= True)
	def __str__(self):
		return "{title}".format(title = self.name)

class Comic(models.Model):

	display_choices= [("M","Manga Style",), ("W","Webtoon Style")]
	status_choices = [("W","Working"),( "H", "On Hold"), ("D", "Dropped"),("I", "Inactive"),("C","Completed")]

	title 					= models.CharField(max_length = 120)
	author					= models.CharField(max_length = 120)
	artist					= models.CharField(max_length = 120)
	description				= models.TextField()
	cover 					= models.ImageField(upload_to="covers/")

	default_display_style	= models.CharField(choices=display_choices, default="W", max_length=1)
	tags					= models.ManyToManyField(Tag, verbose_name="Tags", blank=True)
	discord_role_id			= models.CharField("Discord Role Id", max_length=40)
	status					= models.CharField(choices=status_choices, default="W",max_length=1)

					
	views_cnt				= models.PositiveIntegerField(default = 0)


	def __str__(self):
		return "{title}".format(title = self.title)

	def getLatestChapter(self):
		return Chapter.objects.filter(comic = self).order_by("-pk").first()

	def getAllTags(self):
		return Tag.objects.filter(comic = self).order_by("name")
		
	def get_absolute_url(self):
		return reverse("comic-detail", kwargs = {'pk' : self.pk}) 

	def delete(self, *args, **kwargs):
		self.cover.delete()
		super().delete(*args, **kwargs)

	ordering	=	["title"]


class Chapter(models.Model):
	number 			= models.DecimalField(max_digits = 10,  decimal_places = 2)
	name			= models.CharField(max_length = 120, blank = True, null = True)
	volume			= models.DecimalField(max_digits=3, decimal_places=1, blank = True, null = True)

	views_cnt		= models.PositiveIntegerField(default = 0, null = False)
	updated_at 		= models.DateTimeField(auto_now=True)
	created_at 		= models.DateTimeField(auto_now_add=True)
	comic 			= models.ForeignKey(Comic,on_delete=models.CASCADE)

	def __str__(self):
		return "Chapter {num} | {comic}".format(num= self.number, comic = self.comic)

	def get_absolute_url(self):
		return reverse("chapter-view", kwargs = {'pk' : self.pk}) 

	def getPrevNextCh(self):
		nextCh = Chapter.objects.filter(comic = self.comic, pk__gt=self.pk).order_by('pk').first()
		prevCh = Chapter.objects.filter(comic = self.comic, pk__lt=self.pk).order_by('-pk').first()
		return { 'nextCh': nextCh, 'prevCh': prevCh}


	ordering = ['-number']



class Page(models.Model):

	chapter			= models.ForeignKey(Chapter, on_delete= models.CASCADE)
	image 			= models.ImageField(upload_to = "pages/")
	page_number		= models.PositiveIntegerField()
	updated_at		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{id}'.format(id =self.id)


#Slider Image

class Slide(models.Model):
	comic = models.ForeignKey("Comic", on_delete=models.CASCADE, null = True, blank =True)
	blog_post  = models.ForeignKey("blog.Post", on_delete=models.CASCADE,verbose_name="Blog Post", null= True, blank =True)

	image = models.ImageField(upload_to="Slides/")
	title = models.CharField(blank = True, null =True , max_length=100)
	description = models.TextField(null = True, blank =True)
	link = models.URLField("Hyperlink", max_length=200, blank =True , null =True)
	orderNumber = models.SmallIntegerField("Order Number", unique = True)

