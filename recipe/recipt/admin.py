from django.contrib import admin
from .models import Post, RecipeIngredient, Ingredient, Follow, Comment, Estimation, SubscribeToPost, Tags


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'pub_date', 'author', 'cooking_time', 'image', 'tag') 
    search_fields = ('text',) 
    list_filter = ('pub_date',) 

admin.site.register(Post, PostAdmin)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')

admin.site.register(RecipeIngredient, RecipeAdmin)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')

admin.site.register(Ingredient, IngredientAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')

admin.site.register(Follow, FollowAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','created', 'estimation', 'author', 'post') 

admin.site.register(Comment, CommentAdmin)
admin.site.register(Estimation)

class SubscribeToPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'author', 'post') 

admin.site.register(SubscribeToPost, SubscribeToPostAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',) 

admin.site.register(Tags, TagsAdmin)