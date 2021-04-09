from django import forms
from .models import Subscriber

class Subscriber(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)