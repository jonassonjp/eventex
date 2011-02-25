# -*- coding: utf-8 -*-
import datetime
from django.contrib import admin
# Custom Action
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
# Custom View
from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse

from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
	date_hierarchy = 'created_at'
	search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
	list_filter = ['paid','created_at'] 
	
	actions = ['mark_as_paid']
	
	def mark_as_paid(self, request, queryset):
		count = queryset.update(paid=True)
		
		msg = ungettext(
			u'%(count)d inscrição foi marcada como paga.',
			u'%(count)d inscrições foram marcadas como pagas',
			count
		) % {'count': count}
		self.message_user(request, msg)
	
	mark_as_paid.short_description = _(u"Marcar como pagas")
	
	def export_subscriptions(self, request):
		subscription = self.model.objects.all()
		rows = [','.join([s.name, s.email]) for s in subscription ]
		
		response = HttpResponse('\r\n'.join(rows))
		response.mimetype = "text/csv"
		response['Content-Disposition'] = 'attachment; filename=%s-inscricoes.csv' % datetime.date.today()
		return response
		
	def get_urls(self):
		original_urls = super(SubscriptionAdmin, self).get_urls()
		extra_url = patterns('',
			# Envolvemos nossa view em 'admin_view' por que ela faz o
			# controle de permissões e cache automáticamente para nós.
			url(r'exportar-inscricoes/$',
				self.admin_site.admin_view(self.export_subscriptions), 
				name = 'export_subscriptions')
		)
		# A ordem é impotante. As URLs originais do admin são muito permissivas
		# e acabam sendo encontradas antes da nossa se elas estiverem na frente.
		return extra_url + original_urls

	
	def subscribed_today(self, obj):
		return obj.created_at.date() == datetime.date.today()
	subscribed_today.short_description = 'Inscrito hoje?'
	subscribed_today.boolean = True
	
	
admin.site.register(Subscription, SubscriptionAdmin)