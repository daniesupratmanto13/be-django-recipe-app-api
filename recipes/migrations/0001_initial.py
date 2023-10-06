# Generated by Django 4.2.5 on 2023-10-04 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recipes.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Recipe Category',
                'verbose_name_plural': 'Recipe Categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to='recipes/')),
                ('title', models.CharField(max_length=200)),
                ('descripsion', models.CharField(max_length=200, verbose_name='description')),
                ('cook_time', models.TimeField()),
                ('ingredients', models.TextField()),
                ('procedure', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=models.SET(recipes.models.get_default_recipe_category), to='recipes.recipecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]