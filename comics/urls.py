from django.urls import path
from .views import ( ComicCreateView, ComicListView, ComicUpdateView, comic_detail_view, ComicDeleteView,
  chapter_view, chapter_create_view, ChapterDeleteView)

urlpatterns = [ path('',ComicListView.as_view(), name='comic-view'),
				path('<int:pk>',comic_detail_view, name='comic-detail'),
				path('create/',ComicCreateView.as_view(), name='comic-create'),
				path('update/<int:pk>',ComicUpdateView.as_view(), name='comic-update'),
				path('delete/<int:pk>',ComicDeleteView.as_view(), name='comic-delete'),


				path('chapter/<int:pk>',chapter_view, name='chapter-view'),
				path('<int:pk>/chapter/create/', chapter_create_view, name='chapter-create'),
				path('chapter/delete/<int:pk>',ChapterDeleteView.as_view(), name='chapter-delete')
				
			]