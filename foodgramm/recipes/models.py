from autoslug.settings import slugify
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField
from django.urls import reverse
from unidecode import unidecode

User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(
        'Название ингридиента',
        max_length=150,
        db_index=True
    )
    dimension = models.CharField('Единица измерения', max_length=10)

    class Meta:
        ordering = ('title',)
        verbose_name = 'ингридиент'
        verbose_name_plural = 'ингридиенты'

    def __str__(self):
        return f'{self.title}, {self.dimension}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    title = models.CharField('Название рецепта', max_length=200)
    image = models.ImageField('Изображение', upload_to='recipes/')
    text = models.TextField('Текст рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient'
    )
    cooking_time = models.PositiveIntegerField('Время приготовления')
    slug = AutoSlugField(populate_from='get_unicode_words',
                         allow_unicode=True,
                         unique=True)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    pub_date = models.DateField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )


    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_view_slug', kwargs={'slug': self.slug})

    def get_unicode_words(self):
        return unidecode(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts'
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('ingredient', 'recipe'),
                name='unique_recipe_ingredient'
            )
        ]


class Tag(models.Model):
    title = models.CharField(
        'Имя тега',
        max_length=50,
        db_index=True
    )
    display_name = models.CharField('Имя тега для шаблона', max_length=50)
    color = models.CharField('Цвет тега', max_length=50)

    def __str__(self):
        return self.title
