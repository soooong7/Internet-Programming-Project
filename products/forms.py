from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class SortForm(forms.Form):
    CHOICES = (
        ('asc', '낮은 가격순'),
        ('desc', '높은 가격순'),
    )
    sort_by_price = forms.ChoiceField(choices=CHOICES, required=False)