from . import views
from django.urls import path
from .views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', home, name='home'),
    path('blog_recipes/', views.ListOfRecipes.as_view(), name='blog_recipes'),
    path('create_recipe/', views.add_recipe, name='create_recipe'),
    path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path(
        'delete_recipe/<recipe_id>', views.delete_recipe, name='delete_recipe'
        ),
    path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
    path(
        'delete_comment/<comment_id>', views.delete_comment,
        name='delete_comment'
        ),
    path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico'))),
]
