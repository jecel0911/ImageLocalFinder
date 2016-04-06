from django.shortcuts import render
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CustomUserChangeForm

@login_required()
def profile(request):
	template = loader.get_template('security/profile.html')

	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, request.FILES)
		if form.is_valid():
			custom_user = form.save(commit=False)
		context = {
			'form': form
		}
		return HttpResponseRedirect(reverse('security:profile')) #get the url from urls routing name
	else:
		form = CustomUserChangeForm()
		context = { 'form': form }
		return HttpResponse(template.render(context, request))
	