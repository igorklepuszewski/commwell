from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response

from communication.serializers import BadgeSerializer, FeedbackSerializer, KudosSerializer, KudosCategorySerializer, FeedbackCategorySerializer
from communication.models import Badge, Feedback, Kudos, KudosCategory, FeedbackCategory

# Create your views here.


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class KudosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Kudos.objects.all().select_related("category")
    serializer_class = KudosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Get the sender from the request user
        sender = request.user
        
        # Get the data from the request
        data = request.data.copy()  # make a mutable copy of the request data

        # Add sender to the data
        data['sender'] = sender.id
        
        # Now, use the serializer to validate and create the instance
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Prepare and return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
class BadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [permissions.IsAuthenticated]

class KudosCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = KudosCategory.objects.all()
    serializer_class = KudosCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedbackCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FeedbackCategory.objects.all()
    serializer_class = FeedbackCategorySerializer
    permission_classes = [permissions.IsAuthenticated] 