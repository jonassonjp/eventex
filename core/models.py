# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.db import models
import datetime

class Speaker(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()
  url  = models.URLField(verify_exists=False)
  description = models.TextField(blank=True)
  avatar = models.FileField(upload_to='palestrantes', blank=True, null=True)
  
  def __unicode__(self):
    return self.name
  
class PeriodManager(models.Manager):
  midday = datetime.time(12)
  
  def at_morning(self):
    qs = self.filter(start_time__lt=self.midday)
    qs = qs.order_by('start_time')
    return qs
  
  def at_afternoon(self):
    qs = self.filter(start_time__gte=self.midday)
    qs = qs.order_by('start_time')
    return qs

  
class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind
    
    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs
    
class Contact(models.Model):
    KINDS = (
        ('P', _('Phone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),        
    )
    speaker = models.ForeignKey('Speaker',verbose_name = _('Palestrante'))
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)
    
    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')
    
    
class Talk(models.Model):
  title = models.CharField(_(u'título'), max_length=200)
  description = models.TextField(_(u'descrição'), blank=True)
  start_time = models.TimeField(_(u'horário'), blank=True)
  speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))
  
  objects = PeriodManager()
  
  class Meta:
    verbose_name = _('Palestra')
    
  def __unicode__(self):
    return unicode(self.title)
