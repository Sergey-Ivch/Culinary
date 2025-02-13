from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Ingredient, RecipeIngredient, Follow, User, Comment, SubscribeToPost, Tags
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, CommentForm

NUMBER_OF_POSTS = 6

def get_page(request, post_list): 
    paginator = Paginator(post_list, NUMBER_OF_POSTS) 
    page_number = request.GET.get('page') 
    return paginator.get_page(page_number)

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'recipt/index.html', context)


def spisok_all(request):
    user = request.user
    author_following_posts = Post.objects.filter(subscriptions__user=user)
    context = {
        'posts': author_following_posts,
    }
    return render(request, 'recipt/rkl.html', context)



@login_required
def recipt_all(request):
    keyword = request.GET.get("w", None)
    tag_name = request.GET.get('tag_name') #Get tag_name from GET request

    if keyword:
        posts = Post.objects.filter(name__icontains=keyword)
        tag = None
    
    elif tag_name:
        posts = Post.objects.filter(tag__name=tag_name).order_by('-pub_date')
        tag = Tags.objects.get(name=tag_name)

    else:
        posts = Post.objects.all()
        tag = None

    # if tag_name:
    #     # Filter posts by the selected tag's name
    #     posts = Post.objects.filter(tag__name=tag_name).order_by('-pub_date')
    #     tag = Tags.objects.get(name=tag_name)

    # else:
    #     # Get all posts ordered by publication date (most recent first)
    #     posts = Post.objects.all().order_by('-pub_date')
    #     tag = None

    tags = Tags.objects.all()
    page_obj = get_page(request, posts)
    context = {
        'posts': page_obj,
        'keyword': keyword,
        'selected_tag': tag,
        'tags': tags,
    }
    return render(request, 'recipt/recipt_all.html', context)


@login_required
def recipt_detail(request, recipe_id, username):
    posts = get_object_or_404(Post, id=recipe_id)
    form = CommentForm()
    comments = Comment.objects.filter(post_id=recipe_id)
    recipt = Post.objects.count()
    user = request.user 
    author = get_object_or_404(User, username=username) 
    selected = user.is_authenticated and SubscribeToPost.objects.filter( 
        user=user, author=author, post=recipe_id).exists()
    following = user.is_authenticated and Follow.objects.filter( 
        user=user, author=author).exists()
    context = { 
        'posts': posts,
        'recipt': recipt,
        'recipe_id': recipe_id,
        'following': following,
        'selected':selected,
        'author': author,
        'form': form,
        'comments': comments,
    }
    return render(request, 'recipt/recipt_detail.html', context)


@login_required
def create_recipe(request):
  ingredients = Ingredient.objects.all()
  if request.method == 'POST':
    recipe_form = RecipeForm(request.POST, request.FILES)
    if recipe_form.is_valid():
        post = recipe_form.save(commit=False)
        post.author = request.user
        post.save()
        
        ingredient_data = []
        for i in range(len(request.POST.getlist('ingredient'))):
            ingredient = request.POST.getlist('ingredient')[i]
            quantity = request.POST.getlist('quantity')[i]
            if ingredient and quantity:
                 ingredient_data.append(
                   RecipeIngredient(
                        recipe=post,
                        ingredient_id=int(ingredient),
                        quantity=int(quantity)
                   )
                )
        RecipeIngredient.objects.bulk_create(ingredient_data)
        return redirect('recipt:recipt_all')
  else:
        recipe_form = RecipeForm()
  return render(request, 'recipt/contacts.html', {'form': recipe_form, 'ingredients': ingredients})


@login_required
def edit_recipe(request, recipe_id, username):
    recipe = get_object_or_404(Post, id=recipe_id)
    ingredients = Ingredient.objects.all()
    
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.save()
            RecipeIngredient.objects.filter(recipe=recipe).delete() # Удаление старых ингредиентов

            ingredient_data = []
            for i in range(len(request.POST.getlist('ingredient'))):
                ingredient = request.POST.getlist('ingredient')[i]
                quantity = request.POST.getlist('quantity')[i]
                if ingredient and quantity:
                    ingredient_data.append(
                        RecipeIngredient(
                             recipe=recipe,
                             ingredient_id=int(ingredient),
                             quantity=int(quantity)
                        )
                    )
            RecipeIngredient.objects.bulk_create(ingredient_data)
            return redirect('recipt:recipt_detail', recipe_id=recipe_id, username=username)
    else:
       recipe_form = RecipeForm(instance=recipe)
       initial_ingredient_forms = []
       for recipe_ingredient in RecipeIngredient.objects.filter(recipe=recipe):
            initial_ingredient_forms.append({
                'ingredient': recipe_ingredient.ingredient.id,
                'quantity': recipe_ingredient.quantity,
             })
    
    return render(request, 'recipt/contacts.html', {
            'form': recipe_form, 
            'ingredients': ingredients,
            'initial_ingredient_forms': initial_ingredient_forms, 
            'recipe_id': recipe_id,
            'username': username
        })


@login_required 
def follow_index(request): 
    user = request.user
    author_following_posts = Post.objects.filter( 
        author__following__user=user).all() 
    page_obj = get_page(request, author_following_posts) 
    context = { 
        'page_obj': page_obj 
    }
    return render(request, 'recipt/favourite.html', context) 
 

@login_required 
def profile_follow(request, recipe_id, username): 
    user = request.user 
    author = get_object_or_404(User, username=username) 
    if author != user:
        Follow.objects.get_or_create(
            user=user,
            author=author
        ) 
    return redirect('recipt:recipt_detail', recipe_id=recipe_id, username=username) 
 
 
@login_required
def profile_unfollow(request, recipe_id, username):
    user = request.user
    author = get_object_or_404(User, username=username)
    follower = Follow.objects.filter(user=user, author=author)
    if author != user and follower.exists():
        author.following.filter(user=user, author=author).delete()
    return redirect('recipt:recipt_detail', recipe_id=recipe_id, username=username)



def add_comment(request, recipe_id, username): 
    post = get_object_or_404(Post, id=recipe_id) 
    form = CommentForm(request.POST or None) 
    if form.is_valid(): 
        comment = form.save(commit=False) 
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('recipt:recipt_detail', recipe_id=recipe_id, username=username)


def post_create(request, recipe_id, username): 
    user = request.user 
    post = get_object_or_404(Post, id=recipe_id)
    author = get_object_or_404(User, username=username) 
    if author != user: 
        SubscribeToPost.objects.get_or_create( 
            user=user, 
            post=post,
            author=author
        ) 
    return redirect('recipt:recipt_detail', recipe_id=recipe_id, username=username)



@login_required
def post_delete(request, recipe_id, username):
    user = request.user
    author = get_object_or_404(User, username=username)
    follower = SubscribeToPost.objects.filter(user=user, author=author, post=recipe_id)
    selected_post = get_object_or_404(Post, id=recipe_id)
    if author != user and follower.exists():
        selected_post.subscriptions.filter(user=user, author=author, post=recipe_id).delete()
    return redirect('recipt:spisok_shop')


@login_required
def post_delete_1(request, recipe_id, username):
    user = request.user
    author = get_object_or_404(User, username=username)
    follower = SubscribeToPost.objects.filter(user=user, author=author, post=recipe_id)
    selected_post = get_object_or_404(Post, id=recipe_id)
    if author != user and follower.exists():
        selected_post.subscriptions.filter(user=user, author=author, post=recipe_id).delete()
    return redirect('recipt:recipt_detail', recipe_id=recipe_id, username=username)

