from website.forms import BlogPostForm
from django.shortcuts import render, redirect
from django.utils import timezone

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('website:post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
        return render(request, 'website/post_edit.html', {'form': form})