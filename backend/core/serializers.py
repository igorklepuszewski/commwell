from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    badges_own = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'badges_own']

    def get_badges_own(self, obj):
        return obj.badges_own.all().values_list("id")