# -*- coding: utf-8 -*-	
from django import forms
from django.utils.translation import ugettext as _

from subscription import validators
from subscription.models import Subscription

#class SubscriptionForm(forms.Form):
#	cpf = forms.CharField(label=_('CPF'), 
#		validators=[validators.CPFValidator])	
		



class SubscriptionForm(forms.ModelForm):
	cpf = forms.CharField(label=_('CPF'), 
		validators=[validators.CPFValidator])	
	
	class Meta:
		model = Subscription
		exclude = ('created_at'),('paid'),
		
	def clean(self):
		super(SubscriptionForm, self).clean()
		
		if	not self.cleaned_data.get('email') and \
			not self.cleaned_data.get('phone'): 
				raise forms.ValidationError(
					_(u'Favor informar seu email ou telefone')
				)
		return self.cleaned_data
		
	def _unique_check(self, fieldname, error_message):
		param = { fieldname: self.cleaned_data[fieldname] }
		try:
			s = Subscription.objects.get(**param)
		except Subscription.DoesNotExist:
			return self.cleaned_data[fieldname]
		raise forms.ValidationError(error_message)
		
	def clean_cpf(self):
		return self._unique_check('cpf', _(u'CPF já inscrito'))
		
	def clean_email(self):
		return self._unique_check('email', _(u'E-mail já inscrito'))
