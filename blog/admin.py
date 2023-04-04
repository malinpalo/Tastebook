from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """For Admin to handle Recipes in admin view"""
    list_filter = ('status', 'date_created')
    list_display = ('title', 'slug', 'author', 'date_created')
    search_fields = ['title', 'recipe_description', 'author']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('recipe_ingredients', 'how_to')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """For Admin to manage Comments"""
    list_filter = ('date_created',)
    list_display = ('name', 'share_your_thoughts', 'date_created')
    search_fields = ('name', 'email', 'share_your_thoughts')
