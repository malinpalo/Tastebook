from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """Form for Comments"""
    class Meta:
        model = Comment
        fields = ('share_your_thoughts',)


class RecipeForm(forms.ModelForm):
    """Form for Recipes"""
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'recipe_description',
                  'recipe_ingredients', 'how_to')
        widgets = {
            'recipe_description': SummernoteWidget(),
            'recipe_ingredients': SummernoteWidget(),
            'how_to': SummernoteWidget(),
        }
