from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('recipe/', views.ListOfRecipes.as_view(), name='recipe'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_detail'),
    path('post_recipe/', views.add_recipe, name='post_recipe'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),

]
