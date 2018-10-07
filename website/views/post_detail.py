from django.shortcuts import render, get_object_or_404
from website.models import BlogPost

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'website/post_detail.html', {'post': post})