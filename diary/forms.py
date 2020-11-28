from django import forms
from .models import Diary

class DairyForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('name','content',)