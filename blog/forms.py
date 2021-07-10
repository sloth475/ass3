from django import forms
from django.forms import fields, widgets
from .models import Comment

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=50, error_messages={
#         "required": "Please enter a name",
#         "max_length": "Please enter a shorter name"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=widgets.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=0, max_value=5)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "user_email": "Your email",
            "text": "Your Comment",
            "post":"Choose Post",

        }
        error_messages = {
            "user_name": {
                "required": "Please enter a name",
                "max_length": "Please enter a shorter name"
            }
        }