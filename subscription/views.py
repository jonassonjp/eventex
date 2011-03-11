from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from subscription.forms import SubscriptionForm
from subscription.models import Subscription

def subscribe(request): 
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)

def new(request):
	form = SubscriptionForm(initial={
		'name': 'Seu nome',
		'cpf': 'Digite seu CPF',
		'email': 'Email para contato',
	})
	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html', context)

def create(request):
	form = SubscriptionForm(request.POST)
	
	if not form.is_valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subscription/new.html', context)
	else:
		subscription = form.save()
		if subscription.email!="": 
			sendEmail(subscription)
		return HttpResponseRedirect(reverse('subscription:sucess', args=[ subscription.pk ]))
	


def sucess(request,pk):
	subscription = get_object_or_404(Subscription, pk=pk)
	context = RequestContext(request,{ 'subscription': subscription})
	return render_to_response('subscription/sucess.html', context)


def sendEmail(subscription):
	return send_mail( 
		subject = u'Inscricao no EventeX', 
		message = u'Obrigado '+ subscription.name +' por se inscrever no EventeX!', 
		from_email = 'eventex.jp@gmail.com', 
		recipient_list = [ subscription.email ],
	)