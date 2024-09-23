from communication.models import Kudos
from django_filters import rest_framework as filters

class KudosFilter(filters.FilterSet):
    receiver = filters.NumberFilter(field_name="receiver__id")
    sender = filters.NumberFilter(field_name="sender__id")

    class Meta:
        model = Kudos
        fields = ['receiver', 'sender']