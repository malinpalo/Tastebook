from django.shortcuts import render
from django.views import generic
from .models import Recipe


class List_of_Recipes(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created')
    paginated_by = 8
    template_name = 'recipes.html'
