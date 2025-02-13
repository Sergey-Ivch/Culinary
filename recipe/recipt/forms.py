from django import forms
from .models import Ingredient, RecipeIngredient, Post, Comment, Estimation, User, Tags

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredient'].queryset = Ingredient.objects.all() # Shows the list of ingredients
        self.fields['ingredient'].widget = forms.Select(attrs={'class': 'form-con'})
        self.fields['quantity'].widget = forms.NumberInput(attrs={'class': 'form-control'})


class RecipeForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['name', 'text', 'cooking_time', 'image', 'tag']
    
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'text': forms.Textarea(attrs={'class': 'form-control'}),
      'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
      'image': forms.FileInput(attrs={'class': 'form-control'})
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'].queryset = Tags.objects.all() # Set or override the queryset
        self.fields['tag'].widget = forms.Select()


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['text', 'estimation'] 
        labels = {'text': 'Добавить комментарий'} 
        help_texts = {'text': 'Текст комментария'}
        widgets = {
            'estimation': forms.RadioSelect,
            'text': forms.Textarea(attrs={'class': 'r2r'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estimation'].queryset = Estimation.objects.all() # Set or override the queryset
        self.fields['estimation'].empty_label = None

