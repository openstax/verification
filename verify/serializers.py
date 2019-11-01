from .models import Verification
from rest_framework import serializers
from .tasks import verify_sheerid

class VerificationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        sheerid = verify_sheerid.delay(1)
        verification = Verification.objects.create(**validated_data)
        verification.task_id = sheerid.task_id
        verification.save()
        return verification

    class Meta:
        model = Verification
        fields = ('id', 'salesforce_id', 'ox_accounts_id', 'status', 'created', 'modified', 'accounts_info', 'task_id')
        read_only_fields = ('salesforce_id', 'status', 'task_id')
