from django.urls import path
from . import views

app_name = 'recipt'

urlpatterns = [
    path(
        '', 
        views.index, 
        name='index'
    ),
    path(
        'recipts', 
        views.recipt_all, 
        name='recipt_all'
    ),
    path(
        'recipt/<int:recipe_id>/<str:username>/', 
        views.recipt_detail, 
        name='recipt_detail'
    ),
    path(
        'create/', 
        views.create_recipe, 
        name='create_recipe'
    ),
    path(
        'recipt/<int:recipe_id>/<str:username>/edit/', 
        views.edit_recipe, 
        name='edit_recipe'
    ),
    path(
        'spisok/', 
        views.spisok_all, 
        name='spisok_shop'
    ),
    path( 
        'recipt/<int:recipe_id>/<str:username>/comment/', 
        views.add_comment, 
        name='add_comment'
    ),
    path(
        'recipt/<int:recipe_id>/<str:username>/follow/', 
        views.profile_follow, 
        name='profile_follow' 
    ), 
    path( 
        'recipt/<int:recipe_id>/<str:username>/unfollow/', 
        views.profile_unfollow, 
        name='profile_unfollow' 
    ), 
    path( 
        'spisok/<int:recipe_id>/<str:username>/delete/', 
        views.post_delete, 
        name='post_delete'
    ),
    path( 
        'spisok/<int:recipe_id>/<str:username>/create/', 
        views.post_create, 
        name='post_create' 
    ),
    path( 
        'recipt/<int:recipe_id>/<str:username>/delete/', 
        views.post_delete_1,
        name='post_delete_1'
    ),
    path( 
        'recipt/favourites/', 
        views.follow_index,
        name='follow_index'
    ),
]

