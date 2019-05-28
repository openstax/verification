from .serializers import VerificationSerializer
from .models import Verification

from rest_framework import viewsets



class VerificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = VerificationSerializer
    queryset = Verification.objects.all()