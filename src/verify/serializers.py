from .models import Verification
from rest_framework import serializers


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ('first_name', 'last_name', 'faculty_email_address', 'ox_accounts_id', 'status')
        read_only_fields = ('status', )
