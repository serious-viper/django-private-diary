from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Diary(models.Model):
      name=models.CharField(max_length=30)
      content=RichTextUploadingField(blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      def __str__(self):
            return self.name
      
