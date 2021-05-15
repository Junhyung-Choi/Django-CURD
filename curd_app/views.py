from django.shortcuts import render
from .models import Blog

# Create your views here.
def main(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'curd_app/main.html',context)