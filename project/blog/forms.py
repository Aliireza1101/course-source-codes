from django import forms
from django.db.models import TextChoices
from .models import Comment


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

    def clean_phone_number(self) -> str:
        phone_number: str = self.cleaned_data["phone_number"]
        if phone_number:
            if not phone_number.isnumeric():
                raise forms.ValidationError("This field must be completely numeric!")
            else:
                return phone_number


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
