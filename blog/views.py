from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


def home(request):
    """The home page"""
    return render(request, 'index.html')


class ListOfRecipes(generic.ListView):
    """List of recipes on the webpage, displays 6 per page"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_created')
    template_name = 'blog_recipes.html'
    paginated_by = 6


class RecipeDetail(LoginRequiredMixin, View):
    """
    Views the recipe detail page
    that displays all the recipe details
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        recipe_comments = recipe.recipe_comments.order_by("date_created")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "recipe_comments": recipe_comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        recipe_comments = recipe.recipe_comments.order_by("date_created")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success
            (request, 'Your comment has been successfully added')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "recipe_comments": recipe_comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


@login_required
def add_recipe(request):
    """The view that allows users to create a recipe"""
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.slug = slugify(event.title)
            event.status = 1
            event.save()
            messages.success
            (request, 'Your recipe has been successfully created')
            return redirect('blog_recipes')

    context = {'form': form}
    return render(request, 'create_recipe.html', context)


@login_required
def delete_recipe(request, recipe_id):
    """The view that allows users to delete their recipe"""
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Your recipe was successfully deleted')
    return redirect('blog_recipes')


@login_required
def edit_recipe(request, recipe_id):
    """The view that allows users to update their recipe"""
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(
        request.POST or None, request.FILES or None, instance=recipe)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your recipe was successfully updated')
        return HttpResponseRedirect(
            reverse('recipe_detail', args=[recipe.slug]))
    return render(
        request,
        "edit_recipe.html",
        {
            "recipe": recipe,
            "form": form
        },
    )


@login_required
def delete_comment(request, comment_id):
    """The view that allows users to delete their Comment"""
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    messages.success(request, 'Your comment was successfully deleted')
    return HttpResponseRedirect(
        reverse('recipe_detail', args=[comment.recipe.slug]))


@login_required
def edit_comment(request, comment_id):
    """The view that allows users edit their Comment"""
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your comment was successfully updated')
        return HttpResponseRedirect(
            reverse('recipe_detail', args=[comment.recipe.slug]))
    return render(
        request,
        "edit_comment.html",
        {
            "comment": comment,
            "form": form
        },
    )


class RecipeLike(View):
    """The class view to like and unlike a recipe"""
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
