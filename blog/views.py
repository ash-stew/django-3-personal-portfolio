from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # blogs = Blog.objects.all()  

    # can instead say .order_by('-date')[:5] get most recent 5 most current popup
    # 200 or 300 blogs one page, page take a really long time to load
    blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:7]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #pk primary key. Try grab particular obj for that id, store in blog
    return render(request, 'blog/detail.html', {'blog':blog})
