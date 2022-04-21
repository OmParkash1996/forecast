from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField
from django.utils.timezone import now

class User(AbstractUser):
    class Meta:
        managed = True
        db_table = 'users'

class Forecast(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    forecast = JSONField(blank=True, null=True)
    requested_on = models.DateTimeField(default=now)
    is_emailed = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'forecast'