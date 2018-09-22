from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BettingTip(models.Model):
    home_team = models.CharField(max_length=30)
    away_team = models.CharField(max_length=30)
    prediction = models.CharField(max_length=10)
    odds = models.FloatField()
    analysis = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_title(self):
        return self.home_team + ' - ' + self.away_team + ' (' + self.prediction + ')'

    def __str__(self):
        return self.get_title()
