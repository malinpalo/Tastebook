from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """Model for the recipes"""
    title = models.CharField(max_length=170, unique=True)
    slug = models.SlugField(max_length=170, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_recipes")
    image = CloudinaryField('image', 'placeholder')
    date_created = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    recipe_description = models.TextField()
    recipe_ingredients = models.TextField()
    how_to = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Model for comments"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='recipe_comments')
    name = models.CharField(max_length=90)
    share_your_thoughts = models.TextField()
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Comment {self.share_your_thoughts} written by {self.name}"
