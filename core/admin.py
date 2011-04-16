from django.contrib import admin
from core.models import Speaker, Contact, Talk

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1
    
class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine, ]
    prepopulated_fields = { 'slug': ('name',) }
    
class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_time' )
    

    
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)