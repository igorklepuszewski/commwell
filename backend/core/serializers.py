from rest_framework import serializers

from communication.serializers import BadgeSerializer
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    badges_own = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'badges_own']

    def get_badges_own(self, obj):
        return obj.badges_own.all().values_list("id")
    

class UserDetailSerializer(UserSerializer):
    in_messages_count = serializers.IntegerField(read_only=True)
    out_messages_count = serializers.IntegerField(read_only=True)
    badges_own = BadgeSerializer(many=True)

    class Meta(UserSerializer.Meta):
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + ['in_messages_count', 'out_messages_count']

