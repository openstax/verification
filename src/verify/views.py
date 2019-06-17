from .serializers import VerificationSerializer
from .models import Verification

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class VerificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = (IsAuthenticated,) 
    
    serializer_class = VerificationSerializer
    queryset = Verification.objects.all()