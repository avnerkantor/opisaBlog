from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post

# def home(request):
#     return render_to_response('blog/home.html', {
#     })
#
# def explore(request):
#     return render_to_response('blog/dashboard.html')
#
# def about(request):
#     return render_to_response('blog/about.html')
#


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(posts, 2)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

# def recent(request):
#     posts = Post.objects.all().order_by("-published_date")
#     recentposts = Post.objects.order_by("-published_date")[:5]
#     categories = Category.objects.all()
#     return render_to_response('blog/recentPosts.html',
#                               dict(posts=posts, recentposts=recentposts))
