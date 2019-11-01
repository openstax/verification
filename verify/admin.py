from django.contrib import admin
from .models import Verification

class VerificationAdmin(admin.ModelAdmin):
    list_display = ('ox_accounts_id', 'salesforce_id', 'status')
    list_filter = ('status', )

admin.site.register(Verification, VerificationAdmin)
