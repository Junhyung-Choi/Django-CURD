from django.shortcuts import render, get_object_or_404
from .models import Blog

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