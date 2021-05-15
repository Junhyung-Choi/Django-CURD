from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def main(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'curd_app/main.html',context)

def detail(request,id):
    detail_data = get_object_or_404(Blog,pk=id)
    context = {
        "title": detail_data.title,
        "writer": detail_data.writer,
        "body": detail_data.body,
        "pub_date": detail_data.pub_date,
        "id": detail_data.id,
    }
    return render(request, 'curd_app/detail.html',context)

def create_page(request):
    return render(request, 'curd_app/create.html')

def create(request):
    new_data = Blog()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.body = request.POST['body']
    new_data.pub_date = timezone.now()
    new_data.save()
    return redirect('main')

def update_page(request,id):
    update_data = get_object_or_404(Blog, pk = id)
    context = {
        'id': id,
        'title': update_data.title,
        "writer": update_data.writer,
        "body": update_data.body,
    }
    return render(request,'curd_app/update.html',context)

def update(request,id):
    update_data = get_object_or_404(Blog, pk=id)
    update_data.title = request.POST["title"]
    update_data.writer = request.POST['writer']
    update_data.body = request.POST['body']
    update_data.pub_date = timezone.now()
    update_data.save()
    return redirect('main')

