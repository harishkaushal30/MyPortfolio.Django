from django.shortcuts import render
from blog.models import Comment, Post, PostSection
from blog.forms import  CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    allposts = Post.objects.filter(state='PUBLISHED').order_by('-created_on')
    page = request.GET.get('page', 1)
    paginator = Paginator(allposts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts":posts,
    }
    return render(request, 'home.html', context)

def blog_detail(request, pk):
    post = Post.objects.filter(state="PUBLISHED").get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()
    post_sections = PostSection.objects.filter(post=post).order_by('pk')
    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,
        "form": form,
        "post_sections": post_sections,
    }
    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
        ).filter(state="PUBLISHED").order_by('-created_on')
    context = {
        "posts":posts,
        "category": category,
    }
    return render(request, "blog_category.html", context)

def handler404(request, exception):
    return render(request, "404.html", status=404)

def handler500(request):
    return render(request, "500.html", status=500)