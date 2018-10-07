from django.shortcuts import get_object_or_404, render, redirect
from website.models import BlogPost
from website.forms import BlogPostForm
from django.utils import timezone

def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('website:post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'website/post_edit.html', {'form': form})