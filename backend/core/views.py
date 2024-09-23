from django.shortcuts import render
from rest_framework import permissions, viewsets
from core.serializers import UserDetailSerializer, UserMessageStatsSerializer, UserSerializer
from core.models import User
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response

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
        elif self.action == "message_stats":
            return UserMessageStatsSerializer
        else:
            return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            return super().get_queryset().exclude(id=self.request.user.id)
        return super().get_queryset()

    @action(detail=True, methods=['get'], url_path='message-stats', url_name='message_stats')
    def message_stats(self, request, pk=None):
        # Get the specific user instance
        user = self.get_object()

        # Annotate the user instance with message stats
        annotated_user = User.objects.filter(pk=pk).annotate(
            in_messages_count=Count('kudos_received', distinct=True) + Count('feedback_received', distinct=True),
            out_messages_count=Count('kudos_send', distinct=True) + Count('feedback_send', distinct=True)
        ).values("in_messages_count", "out_messages_count", "id")

        if not annotated_user.exists():
            return Response({"error": "User not found"}, status=404)

        return Response(annotated_user.first())
    
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer