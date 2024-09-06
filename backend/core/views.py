from django.shortcuts import render
from rest_framework import permissions, viewsets
from core.serializers import UserDetailSerializer, UserSerializer
from core.models import User
from django.db.models import Count

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        else:
            return self.serializer_class

    def get_queryset(self):
        if self.action == "retrieve":
            # Annotate the user with received kudos and feedback counts
            return super().get_queryset().annotate(
                in_messages_count=Count('kudos_received', distinct=True) + Count('feedback_received', distinct=True),
                out_messages_count=Count('kudos_send', distinct=True) + Count('feedback_send', distinct=True)
            )
        else:
            return super().get_queryset()