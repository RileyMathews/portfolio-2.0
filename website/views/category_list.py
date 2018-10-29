from django.shortcuts import render
from website.models import BlogPost, Category
from django.utils import timezone

def category_list(request, category):

    current_category = Category.objects.get(name=category)

    posts = BlogPost.objects.filter(categories=current_category.id)
    return render(request, 'website/post_list.html', {'posts': posts})