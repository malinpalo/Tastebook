from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for Comments"""
    class Meta:
        model = Comment
        fields = ('share_your_thoughts',)


class RecipeForm(forms.ModelForm):
    """Form for Recipes"""
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'recipe-description',
                  'recipe-ingredients', 'how-to')
        widgets = {
            'recipe-description': SummernoteWidget(),
            'recipe-ingredients': SummernoteWidget(),
            'how-to': SummernoteWidget(),
        }
