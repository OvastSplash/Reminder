from django import forms
from .models import Reminder
from django.utils import timezone

class ProfileForm(forms.ModelForm):
    message = forms.CharField(max_length=100, label="Task")
    remind_at = forms.DateTimeField(label="Time", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Reminder
        fields = ['message', 'remind_at']

    def clean(self):
        remind_time = self.cleaned_data.get('remind_at')
        message = self.cleaned_data.get('message')
        current_time = timezone.now()

        if remind_time and remind_time <= current_time:
            print(current_time)
            raise forms.ValidationError("Remind time must be in the future")

        if not message:
            raise forms.ValidationError("Message cannot be empty")

        print(current_time)
        print(remind_time)

        return self.cleaned_data