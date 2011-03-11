#encoding: utf-8	
from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import EMPTY_VALUES

from subscription import validators
from subscription.models import Subscription

#class SubscriptionForm(forms.Form):
#	cpf = forms.CharField(label=_('CPF'), 
#		validators=[validators.CPFValidator])	
		

class PhoneWidget(forms.MultiWidget):
	def __init__(self, attrs=None):
		widgets = (
	        forms.TextInput(attrs=attrs),
	        forms.TextInput(attrs=attrs)
	    )
		super(PhoneWidget,self).__init__(widgets,attrs)
		
	def decompress(self, value):
		if value:
			return value.split('-')
		return None, None

class PhoneField(forms.MultiValueField):
	widget = PhoneWidget
	def __init__(self,*args,**kwargs):
		fields = (
	        forms.IntegerField(),
	        forms.IntegerField())
		super(PhoneField, self).__init__(fields, *args, **kwargs)
		
	def compress(self, data_list):
		if data_list:
			if data_list[0] in EMPTY_VALUES:
				raise forms.ValidationError(u'DDD InvÃ¡lido')
			if data_list[1] in EMPTY_VALUES:
				raise forms.ValidationError(u'NÃºmero InvÃ¡lido')
			return '%s-%s' % tuple(data_list)
		return None
	
	def decompress(self, value):
		if value:
			return value.split('-')
		return None, None
	



class SubscriptionForm(forms.ModelForm):
	cpf = forms.CharField(label=_('CPF'), 
		validators=[validators.CPFValidator])	
	phone = PhoneField()
	
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
		

		
		
		
