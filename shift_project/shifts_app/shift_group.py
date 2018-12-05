from django.db import models
from django.utils.timezone import utc, make_aware, get_default_timezone
from datetime import datetime
from django.utils.timezone import now

class ShiftGroupManager(models.Manager):
    pass

    


class ShiftGroup(models.Model):

    #shifts_related

    start_datetime = models.DateTimeField(default=datetime.now,blank=True)
    end_datetime = models.DateTimeField(default=datetime.now,blank=True)

    db_table="shift_group"
    objects = ShiftGroupManager()

    def __str__(self):
        return str(self.start_datetime) + ' - ' + str(self.end_datetime)

    class Meta:
        app_label = "shifts_app"