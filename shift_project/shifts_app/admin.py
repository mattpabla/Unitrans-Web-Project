from django.contrib import admin
from .run import Run
from .shift import Shift
from .shift_group import ShiftGroup


admin.site.register(Run)
admin.site.register(Shift)
admin.site.register(ShiftGroup)
