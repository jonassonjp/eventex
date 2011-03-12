from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from core.models import Speaker

def homepage(request):
  context = RequestContext(request)
  return render_to_response('index.html', context)

def speaker(request, slug):
  speaker = get_object_or_404(Speaker, slug=slug)
  return direct_to_template(request, 'core/speaker.html',
            {'speaker': speaker})
  #context = RequestContext(request, {'speaker':speaker} )
  #return render_to_response('core/speaker.html', context)
  #
  