from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            "user_name": "Your Name:",
            "comment_text": "Your Comment:"
        }

        error_messages = {
            "user_name": {
                "required" : "Your name field must not be emtpy",
                "max_length": "Please enter a shorter name!"
            },
            "comment_text": {
                "required" : "Your comment field must not be emtpy",
                "max_length": "Please enter a shorter comment!",
                "min_length": "Please enter a longer comment!"           
            }
        }
