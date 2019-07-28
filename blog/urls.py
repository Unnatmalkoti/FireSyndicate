from django.urls import path
from .views import BlogListView, post_detail_view

urlpatterns = [ path('',BlogListView.as_view(), name='blog-list'),
                path('<int:pk>', post_detail_view, name='post-detail'),
                ]