from django import forms
from .shift import Shift
from .run import Run
from .shift_group import ShiftGroup

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['start_datetime', 'end_datetime', 'shift_cover','user_id','covered']

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['start_datetime', 'end_datetime']


