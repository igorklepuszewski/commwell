from django.shortcuts import render
from rest_framework import permissions, viewsets
from core.serializers import UserSerializer
from core.models import User

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


#KUDOS, FEEDBACK, KudosCategory, FeedbackCategory, Badge
