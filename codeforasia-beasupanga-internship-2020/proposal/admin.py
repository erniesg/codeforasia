from django.contrib import admin
from .models import Proposal

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost_pax')
    search_fields = ['title']

admin.site.register(Proposal, ProposalAdmin)
