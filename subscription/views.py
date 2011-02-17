from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from subscription.forms import SubscriptionForm
from subscription.models import Subscription

def subscribe(request):
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html', context)


def subscribe(request): 
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html', context)

def create(request):
	form = SubscriptionForm(request.POST)
	
	if not form.is_valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subscription/new.html', context)
	else:
		subscription = form.save()
		return HttpResponseRedirect(reverse('subscription:sucess', args=[ subscription.pk ]))
	


def sucess(request,pk):
	subscription = Subscription.objects.get(id=pk)
	context = RequestContext(request,{ 'subscription': subscription})
	return render_to_response('subscription/sucess.html', context)
