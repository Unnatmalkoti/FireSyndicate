from django.contrib import admin
from .models import Comic, Chapter, Page, Tag, Slide


admin.site.register(Comic)
admin.site.register(Chapter)
admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Slide)

# Register your models here.

