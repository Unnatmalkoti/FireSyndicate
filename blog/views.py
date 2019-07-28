from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post

# Create your views here.

class BlogListView(ListView):
    
	template_name='blog/blog_list.html'
	queryset = Post.objects.all()

def post_detail_view(request,pk):
	current_post = get_object_or_404(Post, pk =pk)
	context = {
		'post': current_post
	}
	return render(request, 'blog/post_detail.html',context, )