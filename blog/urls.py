from . import views
from django.urls import path


urlpatterns = [
    path('recipe/', views.ListOfRecipes.as_view(), name='recipe'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_detail'),

]
