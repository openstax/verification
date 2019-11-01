from django.db import models
from .functions import get_user_info

class Verification(models.Model):
    salesforce_id = models.CharField(max_length=255)
    ox_accounts_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    task_id = models.CharField(max_length=50, unique=True, null=True, blank=True)


    @property
    def accounts_info(self):
        return False
        #return get_user_info(self.ox_accounts_id)

    def __str__(self):
        if self.salesforce_id:
            return self.salesforce_id
        else:
            return self.pk

    class Meta:
        unique_together = ('ox_accounts_id', 'salesforce_id', )


