from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=60)

    post_type_choices = [("R","Recruitment"), ("A","Announcment"),("N","News"),("G","Guide"),("P","Pep Talk")]
    post_type = models.CharField("Type", choices=post_type_choices , max_length=50)

    cover = models.ImageField(upload_to="blog_covers", blank=True, null=True)
    body = RichTextField()
    views = models.PositiveIntegerField("Views", default=0)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})