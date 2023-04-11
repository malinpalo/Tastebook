from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('recipe/', views.ListOfRecipes.as_view(), name='recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('post_recipe/', views.add_recipe, name='post_recipe'),
    path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
    path(
        'delete_recipe/<recipe_id>', views.delete_recipe, name='delete_recipe'
        ),
    path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),

]
