from django.db import models
from .functions import get_user_info

class Verification(models.Model):
    salesforce_id = models.CharField(max_length=255)
    ox_accounts_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return ''

    @property
    def fullname(self):
        return ''

    def __str__(self):
        return self.salesforce_id

    class Meta:
        unique_together = ('ox_accounts_id', 'salesforce_id', )