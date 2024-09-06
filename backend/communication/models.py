from django.db import models

from core.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        abstract=True

    def __str__(self):
        return self.name

class KudosCategory(Category):
    pass

class FeedbackCategory(Category):
    pass

class Message(models.Model):
    
    message = models.TextField(max_length=500)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_received")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messsages_send")
    is_read = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Kudos(Message):
    category = models.ForeignKey(KudosCategory, on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kudos_received")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="kudos_send")

    def __str__(self):
        return f"Kudos ID:{self.id} from {self.sender} to {self.receiver}"

class Feedback(Message):
    category = models.ForeignKey(FeedbackCategory, on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_received")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_send")


    def __str__(self):
        return f"Feedback {self.id} from {self.sender} to {self.receiver}"


class Badge(models.Model):
    owners = models.ManyToManyField(User, blank=True)
    badge_name = models.CharField(max_length=40)
    badget_picture = models.ImageField(blank=True, null=True)
    required_kudos = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(KudosCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.badge_name} - {self.category}"

