from .serializers import VerificationSerializer
from .models import Verification

from django.http import JsonResponse
from django.views import View

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from celery.result import AsyncResult


class VerificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing faculty verification instances.
    """
    #permission_classes = (IsAuthenticated,)
    
    serializer_class = VerificationSerializer
    queryset = Verification.objects.all().order_by('-created')

    def get_queryset(self):
        queryset = Verification.objects.all()
        ox_accounts_id = self.request.query_params.get('ox_accounts_id', None)
        if ox_accounts_id is not None:
            queryset = queryset.filter(ox_accounts_id=ox_accounts_id)
        return queryset


class TaskView(View):
    def get(self, request, task_id):
        task = AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            response_data['results'] = task.get()

        return JsonResponse(response_data)
