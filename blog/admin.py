from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """For Admin to handle Recipes in admin view"""
    summernote_fields = ('recipe_ingredients', 'how_to')
