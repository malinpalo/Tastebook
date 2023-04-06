from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


def home(request):
    """ The home page """
    return render(request, 'index.html')


class ListOfRecipes(generic.ListView):
    """List of recipes on the webpage, displays 6 per page"""
    template_name = 'recipe.html'
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created')
    paginated_by = 6


class RecipeDetails(View):
    """
    Views the recipe detail page
    that displays all the recipe details
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by("date_added")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
