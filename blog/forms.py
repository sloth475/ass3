from typing import List

from django import forms
from django.forms import fields, widgets
from .models import Comment,Post

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
        exclude = ["post"]
        # fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "user_email": "Your email",
            "text": "Your Comment",


        }
        error_messages = {
            "user_name": {
                "required": "Please enter a name",
                "max_length": "Please enter a shorter name"
            }
        }

class UploadForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= "__all__"
