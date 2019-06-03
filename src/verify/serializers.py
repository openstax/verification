from .models import Verification
from rest_framework import serializers


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('salesforce_id', 'ox_accounts_id', 'status', 'created', 'modified')
        read_only_fields = ('salesforce_id', 'status', )
