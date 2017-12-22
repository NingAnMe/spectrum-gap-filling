import markdown

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    '''
    文章详情页
    '''
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ],)
    return render(request, 'blog/detail.html', context={'post': post})

def archives(request, year, month):
    '''
    文章归档页
    '''
    post_list = Post.objects.filter(
                                    created_time__month=month,
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    '''
    文章分类页
    '''
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
