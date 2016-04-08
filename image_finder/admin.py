from django.contrib import admin
from .models import *

class ImageDetailInline(admin.TabularInline):
	model = ImageDetail
	extra = 1
class ImageHeaderAdmin(admin.ModelAdmin):
	list_display = ('description','date_added','resolved')
	inlines = [ImageDetailInline]

admin.site.register(ImageHeader)
admin.site.register(ImageDetail)