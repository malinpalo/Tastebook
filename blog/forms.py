from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for Comments"""
    class Meta:
        model = Comment
        fields = ('share_your_thoughts',)
