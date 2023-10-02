from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))
    slug = models.SlugField(
        max_length=120, null=False, blank=True, unique=True, editable=False
    )

    class Meta:
        verbose_name = _('Recipe Category')
        verbose_name_plural = _('Recipe Categories')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


def get_default_recipe_category():

    return RecipeCategory.objects.get_or_create(name='Others')[0]


class Recipe(models.Model):
    author = models.ForeignKey(
        User, related_name="recipes", on_delete=models.CASCADE)
    category = models.ForeignKey(
        RecipeCategory, on_delete=models.SET(get_default_recipe_category))
    picture = models.ImageField(upload_to="recipes/")
    title = models.CharField(max_length=200)
    descripsion = models.CharField(_('description'), max_length=200)
    cook_time = models.TimeField()
    ingredients = models.TextField()
    procedure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.CharField(
        choices=LIKE_CHOICES, default='Like', max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} {self.value} {self.recipe}'