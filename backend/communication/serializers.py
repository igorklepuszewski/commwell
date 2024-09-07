from rest_framework import serializers

from communication.models import Badge, Feedback, Kudos, KudosCategory, FeedbackCategory


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["category", "receiver", "sender"]

class KudosSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Kudos
        fields = ["category", "receiver", "sender"]

    def get_category_name(self):
        return self.category.name

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ["owners", "badge_name", "badge_picture", "required_kudos", "category"]


class KudosCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KudosCategory
        fields = ["id", "name"]

class FeedbackCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackCategory
        fields = ["id", "name"]        