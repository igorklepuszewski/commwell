from rest_framework import permissions, viewsets

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
    queryset = Kudos.objects.all()
    serializer_class = KudosSerializer
    permission_classes = [permissions.IsAuthenticated]
    
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