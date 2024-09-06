from django.contrib import admin

from communication.models import Feedback, FeedbackCategory, Kudos, KudosCategory

# Register your models here.


admin.site.register(Kudos)
admin.site.register(KudosCategory)
admin.site.register(Feedback)
admin.site.register(FeedbackCategory)
