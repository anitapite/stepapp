from django.conf import settings
from django.db import models
from django.utils import timezone



class Step(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    monday_stepcount = models.IntegerField()
    monday_activities = models.CharField(max_length=32, blank=True)
    monday_date = models.DateField()
    tuesday_stepcount = models.IntegerField()
    tuesday_activities = models.CharField(max_length=32, blank=True)
    tuesday_date = models.DateField()
    wednesday_stepcount = models.IntegerField()
    wednesday_activities = models.CharField(max_length=32, blank=True)
    wednesday_date = models.DateField()
    thursday_stepcount = models.IntegerField()
    thursday_activities = models.CharField(max_length=32, blank=True)
    thursday_date = models.DateField()
    friday_stepcount = models.IntegerField()
    friday_activities = models.CharField(max_length=32, blank=True)
    friday_date = models.DateField()
    saturday_stepcount = models.IntegerField()
    saturday_activities = models.CharField(max_length=32, blank=True)
    saturday_date = models.DateField()
    sunday_stepcount = models.IntegerField()
    sunday_activities = models.CharField(max_length=32, blank=True)
    sunday_date = models.DateField()
    notes = models.CharField(max_length=256, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.stepcount