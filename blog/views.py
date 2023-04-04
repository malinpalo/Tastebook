from django.shortcuts import render
from django.views import generic
from .models import Recipe


class ListOfRecipes(generic.ListView):
    template_name = 'recipe.html'
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created')
    paginated_by = 6
