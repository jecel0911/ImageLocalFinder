from django.db import models

#List of files uploade
class FileUploaded(models.Model):
	bytes = models.TextField()
	filename = models.CharField(max_length=255)
	mimetype = models.CharField(max_length=50)