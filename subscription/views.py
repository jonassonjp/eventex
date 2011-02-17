from django.shortcuts import render_to_response
from django.template import RequestContext

def subscribe(request):
	context = RequestContext(request)
	return render_to_response('new.html', context)
