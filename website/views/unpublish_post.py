from website.models import BlogPost
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

def unpublish_post(request, pk):
    """publishes a post based on the primary key sent in the url
    
    Arguments:
        request {http request} -- the full http request object
        pk {primary key} -- the primary key of the post to be published
    
    Returns:
        http request -- returns an error page or the detail page of the newly published post
    """
    post = get_object_or_404(BlogPost, pk=pk)
    post.unpublish()
    return redirect('website:post_detail', pk=post.pk)
