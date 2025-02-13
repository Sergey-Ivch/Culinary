from django.db import models
from recipt.validators import validate_not_empty, validate_capitalized, validate_non_negative
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200
    )

    measurement_unit = models.CharField(
        'Единица измерения',
        default='г',
        max_length=10
    )

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(
        'Название',
        max_length=40,
        default='Легко'
    )
    
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        validators=[validate_not_empty, validate_capitalized]
    )

    text = models.TextField(
        'Описание',
        validators=[validate_not_empty, validate_capitalized]
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации' # Added verbose name for clarity
    )

    cooking_time = models.IntegerField(
        'Время приготовления, мин',
        validators=[validate_non_negative, validate_not_empty],
        help_text='Укажите время в минутах' # Added help text for user guidance
    )
    
    tag = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE,
        related_name='tags', #Changed to a more descriptive related_name. Avoids reverse accessor clashes.
        verbose_name='сложность',
        null=True

    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор' #Added verbose_name
    )

    image = models.ImageField(
        'Картинка',
        upload_to='recipes/', #Changed to a more semantic name.  Avoid "spicok" unless it has a specific meaning.
        blank=True,
        null=True #Added null=True to allow no image. Best practice with blank=True.
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient', #Renamed to singular to match convention
        through_fields=('recipe', 'ingredient'),
        verbose_name='Ингредиенты'
    )

    class Meta:
        verbose_name = 'Рецепт' # Added verbose name for model clarity
        verbose_name_plural = 'Рецепты' # Added plural verbose name

    def __str__(self):
      return self.name


class RecipeIngredient(models.Model): #Renamed to singular
    recipe = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients', #Changed to a more descriptive related_name. Avoids reverse accessor clashes.
        verbose_name='Рецепт'
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipt', #Changed to a more descriptive related_name. Avoids reverse accessor clashes.
        verbose_name='Ингредиент'
    )
    quantity = models.PositiveIntegerField( #Changed to positive integer field
        'Количество',
        default=1,
        validators=[validate_non_negative],
        help_text='Укажите количество ингредиента' #Added help text for user
    )
    

    class Meta:
        verbose_name = 'Ингредиент в рецепте' #Added for clarity
        verbose_name_plural = 'Ингредиенты в рецептах' #Added for clarity
        unique_together = ('recipe', 'ingredient') #Avoid duplicates

    def __str__(self):
        return f"{self.quantity} {self.ingredient.measurement_unit} {self.ingredient.name} в {self.recipe.name}" #More descriptive string representation



class Estimation(models.Model):
    estimation = models.CharField(
        'Оценка',
        max_length=1,
        help_text='Оценка от 1 до 5'
    )

    class Meta:
      verbose_name = 'Оценка'
      verbose_name_plural = 'Оценки'


    def __str__(self):
        return self.estimation


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Рецепт' #Added verbose_name
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор' #Added verbose_name
    )
    estimation = models.ForeignKey(
        Estimation,
        on_delete=models.CASCADE,
        related_name='comments', #Changed to a more descriptive related_name. Avoids reverse accessor clashes.
        verbose_name='Оценка' #Added verbose_name
    )
    text = models.TextField(
        'Текст комментария' #Added verbose_name
    )
    created = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created'] #Order comments by creation date (most recent first)

    def __str__(self):
        return self.text 

 
class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text = 'Пользователь, на которого подписываются'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'author')  # Prevent duplicate follows

    def __str__(self):
        return f'{self.user.username} подписан на {self.author.username}'


class SubscribeToPost(models.Model): 
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        verbose_name='Подписчик', 
        related_name='post_subscriptions' 
    )
    author = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE, 
        related_name='f', 
        verbose_name='Создатель постов'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='subscriptions', #Changed related_name for clarity and to avoid clashes
        verbose_name='Пост'
    )

    class Meta:
      verbose_name = 'Подписка на пост'
      verbose_name_plural = 'Подписки на посты'
    

    def __str__(self):
        return f'{self.user.username} подписан на {self.post.name}'