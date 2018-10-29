from django.shortcuts import render
from website.models import BlogPost
from django.utils import timezone

def post_list(request):

    # filter out posts by superuser status to show unpublished posts
    if request.user.is_superuser:
        posts = BlogPost.objects.all().order_by('published_date')
    else:
        posts = BlogPost.objects.filter(published_date__isnull=False).order_by('published_date')

    return render(request, 'website/post_list.html', {'posts': posts})