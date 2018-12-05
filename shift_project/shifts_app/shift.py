from django.db import models
from django.db.models import Q
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime
from datetime import date

from shifts_app.shift_group import ShiftGroup

class ShiftManager(models.Manager):

    def create_shift(self, start_datetime, end_datetime, run_times_list):
        #run_times_list -> [{start_time=time, end_time=time},{...},{...}]
        from shifts_app.run import Run
        from shifts_app.shift_group import ShiftGroup
        runs_to_create = []


        #try to condense or find better solution 
    #iterates through the groups objects and chekcks if its start_datetime weekday is the same as the one in the create_shift()...
    #...if it is then we create a new shift_instance with the attached group of the same weekday and if not then a new group gets created
        all_groups = ShiftGroup.objects.all()
        for group in all_groups:
            if(start_datetime.date.weekday() == 0 and group.start_datetime.date.weekday() == 0):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break
            
            elif(start_datetime.date.weekday() == 1 and group.start_datetime.date.weekday() == 1):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break

            elif(start_datetime.date.weekday() == 2 and group.start_datetime.date.weekday() == 2):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break

            elif(start_datetime.date.weekday() == 3 and group.start_datetime.date.weekday() == 3):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break

            elif(start_datetime.date.weekday() == 4 and group.start_datetime.date.weekday() == 4):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break

            elif(start_datetime.date.weekday() == 5 and group.start_datetime.date.weekday() == 5):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break

            elif(start_datetime.date.weekday() == 6 and group.start_datetime.date.weekday() == 6):
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=group)
                break

            else:
                shift_group_instance = ShiftGroup.objects.create(start_datetime=start_datetime, end_datetime=end_datetime)
                shift_instance = self.create(start_datetime=start_datetime, end_datetime=end_datetime, shift_group=shift_group_instance)
                break
        
        


        last_end_date = start_datetime.date()

        for run_times_dict in run_times_list:

            run_start_datetime = make_aware( datetime.datetime.combine(last_end_date, run_times_dict['start_time']), get_default_timezone() ).astimezone(utc)
            run_end_datetime = make_aware(datetime.datetime.combine(last_end_date, run_times_dict['end_time']), get_default_timezone()).astimezone(utc)
            if run_start_datetime > run_end_datetime:
                run_end_datetime += datetime.timedelta(days=1)
            last_end_date = run_end_datetime.date()

            runs_to_create.append(Run(
                shift=shift_instance,
                start_datetime=run_start_datetime,
                end_datetime=run_end_datetime
            ))
        Run.objects.bulk_create(runs_to_create)

        return shift_instance



    def get_shifts_in_datetime_range(self, start_datetime, end_datetime):
        return self.filter(
                    Q(start_datetime__lte=start_datetime, end_datetime__gte=start_datetime)
                    | Q(start_datetime__lte=end_datetime, end_datetime__gte=end_datetime)
                    | Q(start_datetime__gte=start_datetime, end_datetime__lte=end_datetime)
                    | Q(start_datetime__lte=start_datetime, end_datetime__gte=end_datetime)
                )



class Shift(models.Model):

    #runs_related

    db_table="shift"
    objects = ShiftManager()

    #shift_group  = models.ForeignKey(ShiftGroup, related_name="shifts_related")
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    shift_cover = models.BooleanField(default = False)
    user_id = models.CharField(max_length=200)
    covered = models.BooleanField(default = False)

    def __str__(self):
        return str(self.start_datetime) + ' - ' + str(self.end_datetime)

    class Meta:
        app_label = "shifts_app"
