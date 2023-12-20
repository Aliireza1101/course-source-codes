from django import forms
from django.db.models import TextChoices
from better_profanity import profanity

from .models import Comment, Post


# Create your forms here.
class TicketForm(forms.Form): # Form to create a ticket
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


class CommentForm(forms.ModelForm): # Form to create a comment
    class Meta:
        model = Comment
        fields = ("text",)


class PostForm(forms.ModelForm):  # Form to create a post
    class Meta:
        fields = ["title", "description", "reading_time"]
        model = Post

    def clean_title(self):  # validation for title
        title: str = self.cleaned_data["title"]
        if profanity.contains_profanity(title):
            raise forms.ValidationError("Your title can't contain profanity!")

        words = title.split(" ")
        for word in words:
            # Longest word in english = 'pneumonoultramicroscopicsilicovolcanoconiosis' (45 letters) :))
            if len(word) > 45:
                raise forms.ValidationError(f"The word '{word}' is too long!")

        return title
