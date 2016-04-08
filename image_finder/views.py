from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UploadForm
#from .models import Attachment

def image_finder_index(request):
	template = loader.get_template('image_finder/image_finder_index.html')
	context = {}
	return HttpResponse(template.render(context, request))


'''
	if request.method == 'GET':
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect(reverse('profiles:candidate_profile')) #get the url from urls routing name
'''


'''
class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)
'''