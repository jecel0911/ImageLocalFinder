from django.db import models
import time
import random
from functools import partial


def _update_filename(instance, filename, path):
	return path + str(time.time()) + '_' + str(random.randint(0,1000)) + '_' + filename

def upload_to(path):
    return partial(_update_filename, path=path)

# Create your models here.
class ImageHeader(models.Model):
	description = models.TextField()
	date_added = models.DateTimeField()
	resolved = models.BooleanField(default=False)

	def __unicode__(self):
		return self.description

	def __str__(self):
		return self.__unicode__()


class ImageDetail(models.Model):
	image_header = models.ForeignKey(ImageHeader)
	image = models.FileField(upload_to=upload_to('ImageLocalFinder/static/attachments/'))
	resolved = models.BooleanField()



	def __unicode__(self):
		return 'Image ' + str(self.id)

	def __str__(self):
		return self.__unicode__()