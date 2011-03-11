# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.db import models

class Speaker(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()
  url  = models.URLField(verify_exists=False)
  description = models.TextField(blank=True)
  avatar = models.FileField(upload_to='palestrantes', blank=True, null=True)
  
  def __unicode__(self):
    return self.name
  
  def __init__(self):
    """Constructor Speaker Class"""
    
    
    
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
    

class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind
    
    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs