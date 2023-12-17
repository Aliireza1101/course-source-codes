from django import forms
from django.db.models import TextChoices


class TicketForm(forms.Form):
    class Subject(TextChoices):
        proposal = "PP", "Proposal"
        feedback = "FB", "Feedback"
        report = "RP", "Report"

    title = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    subject = forms.ChoiceField(choices=Subject.choices, required=True)
    
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
