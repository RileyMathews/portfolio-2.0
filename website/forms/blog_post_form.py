from django import forms
from website.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'subtitle', 'text', 'categories',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'text-input'}),
            'subtitle': forms.TextInput(attrs={'class': 'text-input'}),
            'text': forms.Textarea(attrs={'class': 'text-area'}),
            'categories': forms.SelectMultiple(attrs={'class': 'input-select'}),
        }