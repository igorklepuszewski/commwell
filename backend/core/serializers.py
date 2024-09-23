from rest_framework import serializers

from communication.serializers import BadgeSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    badges_own = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'badges_own']

    def get_badges_own(self, obj):
        return obj.badges_own.all().values_list("id")
    

class UserDetailSerializer(UserSerializer):
    badges_own = BadgeSerializer(many=True)

class UserMessageStatsSerializer(UserSerializer):
    in_messages_count = serializers.IntegerField(read_only=True)
    out_messages_count = serializers.IntegerField(read_only=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = ["id", "in_messages_count", "out_messages_count"]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        return data

    

