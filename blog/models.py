from django.db import models
import uuid
from django.urls import reverse
from ckeditor.fields import RichTextField


class Project(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.TextField(max_length=80)
    body = RichTextField(max_length=10000)
    project_type = models.TextField(max_length=50,null=True)
    cover = models.ImageField(upload_to="media",blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("project_detail", args=[str(self.id)])
class Link(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="links")
    link = models.URLField()

class Image(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="images")
    image = models.URLField(blank=True)
