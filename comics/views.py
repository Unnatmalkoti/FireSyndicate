from PIL import Image
from django.shortcuts import render,get_object_or_404, redirect

from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import ChapterCreateForm, ChapterImagesForm, ComicCreateForm, ChapterZipForm
from .models import Chapter,Comic,Page, Slide

from BackgorundService import sendNotif
from helperFunctions import saveChapter


def home_view(request):
	
	SearchQuery= request.GET.get("query")
	if SearchQuery:
		SearchQuerySet = Comic.objects.filter(title__icontains= SearchQuery)
		context = {
			"SearchQuerySet": SearchQuerySet
		}
	else:
		qs3 = Slide.objects.order_by("orderNumber")
		qs = Chapter.objects.order_by("-created_at")[0:5]
		qs2 = Comic.objects.order_by("-views_cnt")[0:10]
		context = {
			"LatestChapters" : qs,
			"PopularComics" : qs2,
			"Slides":qs3,
		}

	return render(request, 'comics/home.html',context)


##Comic - Views

class ComicListView(ListView):

	template_name='comics/comic_list.html'
	queryset = Comic.objects.all()


#Comic Detail View
def comic_detail_view(request, pk):
	current_comic = get_object_or_404(Comic, pk =pk)
	current_comic.views_cnt += 1
	current_comic.save()
	queryset = Chapter.objects.filter(comic = current_comic).order_by("-created_at")

	context = {
	'object_data'	: current_comic,
	'queryset'		: queryset
	}
	return render(request, 'comics/comic_detail.html', context)

#Comic Create View
class ComicCreateView(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	form_class = ComicCreateForm
	template_name = "comics/comic_create.html"

#Comic Update View
class ComicUpdateView(LoginRequiredMixin,CreateView):
	template_name = "comics/comic_create.html"
	form_class = ComicCreateForm
	model = Comic
	login_url = '/login/'
	redirect_field_name = ''


#Comic Delete View
class ComicDeleteView( LoginRequiredMixin,DeleteView):
	login_url = '/login/'
	redirect_field_name = ''
	queryset = Comic.objects.all()
	template_name = "comics/comic_delete.html"

	def get_success_url(self):
		return reverse('comic-view')




##Chapter - Views

#Chapter View
def chapter_view(request, pk):
	
	current_chapter = get_object_or_404(Chapter, pk = pk)
	queryset = Page.objects.filter(chapter = current_chapter)
	current_comic = current_chapter.comic
	
	current_comic.views_cnt += 1
	current_chapter.views_cnt += 1

	prevNext = current_chapter.getPrevNextCh()
	current_chapter.save()
	current_comic.save()

	context = {
	'object_data'	: current_chapter,
	'queryset'		: queryset,
	'prevCh'	: prevNext['prevCh'],
	'nextCh'	: prevNext['nextCh'],
	}
	print (queryset)
	return render(request, 'comics/comic_viewer.html', context)



#Chapter Create View
def chapter_create_view(request, pk):
	if request.user.is_authenticated is not True:
		raise Http404

	current_comic = get_object_or_404(Comic, pk = pk)
	if (request.POST):
		#file_form = ChapterZipForm(request.POST or None, request.FILES or None, images= request.FILES.getlist("images") or None)
		file_form = ChapterZipForm(request.POST or None, request.FILES or None)
		form = ChapterCreateForm(request.POST or None)
		
		#image_files = request.FILES.getlist("images")
		saveChapter.save(fileForm = file_form, chapterForm = form, request = request)
		# if form.is_valid() and file_form.is_valid():

		# 	saved_chapter = form.save()
		# 	countr = 1
		# 	for file in image_files:
		# 		temp_page = Page(image=file, chapter = saved_chapter, page_number= countr)
		# 		countr = countr + 1
		# 		temp_page.save()

		# 	sendNotif.send(saved_chapter)
		# 	return redirect("chapter-view",saved_chapter.pk)
			
	else:
		form = ChapterCreateForm(initial={'comic': current_comic})
		#file_form = ChapterImagesForm()
		file_form = ChapterZipForm()

	
	context = {
	 	'form' :form,
	 	'file_form' :file_form
	}


	return render(request, 'comics/chapter_create.html', context)

#Chapter Delete View
class ChapterDeleteView(LoginRequiredMixin,DeleteView):
	queryset = Chapter.objects.all()
	template_name = "comics/comic_delete.html"
	login_url = '/login/'
	redirect_field_name = ''

	def get_success_url(self):
		return reverse('comic-view')


################################################
#Testing stuff
################################################

def test_view(request):
	return render(request,'comics/test.html',{})


