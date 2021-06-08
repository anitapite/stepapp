from django.conf import settings
from django.db import models
from django.utils import timezone


class Step(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    stepcount = models.IntegerField()
    activities = models.CharField(max_length=32)
    notes = models.CharField(max_length=256, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.stepcount