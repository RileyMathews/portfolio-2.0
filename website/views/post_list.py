from django.shortcuts import render
from website.models import BlogPost
from django.utils import timezone

def post_list(request):
    posts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/post_list.html', {'posts', posts})