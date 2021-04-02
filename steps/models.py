from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stepcount = models.IntegerField()
    activities = models.CharField(max_length=32)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.stepcount