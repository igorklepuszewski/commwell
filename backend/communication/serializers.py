from rest_framework import serializers

from communication.models import Badge, Feedback, Kudos


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["category", "receiver", "sender"]

class KudosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kudos
        fields = ["category", "receiver", "sender"]

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ["owners", "badge_name", "badge_picture", "required_kudos", "category"]
