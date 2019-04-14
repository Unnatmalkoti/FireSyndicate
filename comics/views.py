from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import ChapterCreateForm, ChapterImagesForm, ComicCreateForm, LoginForm
from .models import Chapter,Comic,Page

def home_view(request):
	qs = Chapter.objects.order_by("-created_at")[0:5]
	qs2 = Comic.objects.order_by("-views_cnt")[0:10]

	print (qs)
	print ("hi")
	context = {
	"LatestChapters" : qs,
	"PopularComics" : qs2
	}
	return render(request, 'comics/home.html',context)

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
	Login_url = '/login/'
	redirect_field_name = ''
	template_name = "comics/comic_create.html"
	form_class = ComicCreateForm

#Comic Update View
class ComicUpdateView(LoginRequiredMixin,CreateView):
	template_name = "comics/comic_create.html"
	form_class = ComicCreateForm
	login_url = '/login/'
	redirect_field_name = ''

#Comic Delete View
class ComicDeleteView( LoginRequiredMixin,DeleteView):
	login_url = '/login/'
	redirect_field_name = ''
	queryset = Comic.objects.all()
	template_name = "comics/comic_delete.html"

	def get_success_url(self):
		return reverse('comic-list')

#Chapter View
def chapter_view(request, pk):
	
	current_chapter = get_object_or_404(Chapter, pk = pk)
	queryset = Page.objects.filter(chapter = current_chapter)
	current_comic = current_chapter.comic

	current_comic.views_cnt += 1
	current_chapter.views_cnt += 1
	
	current_chapter.save()
	current_comic.save()

	context = {
	'object_data'	: current_chapter,
	'queryset'		: queryset
	}
	print (queryset)
	return render(request, 'comics/comic_viewer.html', context)



#Chapter Create View
def chapter_create_view(request, pk):
	if request.user.is_authenticated is not True:
		raise Http404
	current_comic = get_object_or_404(Comic, pk = pk)
	if (request.POST):
		file_form = ChapterImagesForm(request.POST or None)
		form = ChapterCreateForm(request.POST or None)
		form.comic = current_comic
		
		print (file_form)

		if form.is_valid():
			saved_chapter = form.save()
			image_files = request.FILES.getlist("images")

			countr = 1
			for file in image_files:
				temp_page = Page(image=file, chapter = saved_chapter, page_number= countr)
				countr = countr + 1
				temp_page.save()

			#return HttpResponseRedirect(saved_chapter.get_absolute_url) 	
	else:
		form = ChapterCreateForm(initial={'comic': current_comic})
		file_form = ChapterImagesForm()

	
	context = {
	 	'form' :form,
	 	'file_form' :file_form
	}


	return render(request, 'comics/chapter_create.html', context)

#Comic Delete View
class ChapterDeleteView(LoginRequiredMixin,DeleteView):
	queryset = Chapter.objects.all()
	template_name = "comics/comic_delete.html"
	login_url = '/login/'
	redirect_field_name = ''

	def get_success_url(self):
		return reverse('comic-view')


