from django.contrib import admin
from core.models import Speaker, Contact

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1
    
class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine, ]
    prepopulated_fields = { 'slug': ('name',) }
    
admin.site.register(Speaker, SpeakerAdmin)