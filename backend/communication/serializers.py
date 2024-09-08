from rest_framework import serializers

from communication.models import Badge, Feedback, Kudos, KudosCategory, FeedbackCategory


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["category", "receiver", "sender"]


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ["owners", "name", "picture", "required_kudos", "category"]


class KudosCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KudosCategory
        fields = ["id", "name"]

class FeedbackCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackCategory
        fields = ["id", "name"]  
      
class KudosSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Kudos
        fields = ["category", "receiver", "sender", "message"]

    def get_category(self, obj):
        """
        This method will be called when serializing data for GET requests.
        It returns the nested category details.
        """
        return KudosCategorySerializer(obj.category).data

    def to_internal_value(self, data):
        """
        This method handles the deserialization for POST requests.
        It accepts the category ID and maps it to the related category.
        """
        internal_data = super().to_internal_value(data)
        category_id = data.get('category')

        # Validate and assign the category ID
        try:
            internal_data['category'] = KudosCategory.objects.get(id=category_id)
        except KudosCategory.DoesNotExist:
            raise serializers.ValidationError({"category": "Invalid category ID."})
        
        return internal_data