from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/details.html', {'post': post})

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Новые сверху
    paginator = Paginator(posts, 3)  # 3 постов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'blog/post_list.html', context)