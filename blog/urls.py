from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    
    path('blog_recipes/', views.ListOfRecipes.as_view(), name='blog_recipes'),
    path('create_recipe/', views.add_recipe, name='create_recipe'),
    path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
    path(
        'delete_recipe/<recipe_id>', views.delete_recipe, name='delete_recipe'
        ),
    path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
    path(
        'delete_comment/<comment_id>', views.delete_comment,
        name='delete_comment'
        ),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),

]
