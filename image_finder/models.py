from django.db import models
from file_upload.models import FileUploaded

# Create your models here.
class ImageHeader(models.Model):
	description = models.TextField()
	date_added = models.DateTimeField()
	resolved = models.BooleanField(default=False)

class ImageDetail(models.Model):
	image = models.FileField(upload_to='file_upload.FileUploaded/bytes/filename/mimetype')
	resolved = models.BooleanField()
