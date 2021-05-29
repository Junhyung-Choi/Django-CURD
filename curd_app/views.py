from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,Store,Comment
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def main(request):
    blogs = Blog.objects.all()
    stores = Store.objects.all()
    context = {
        "stores": stores,
    }
    return render(request, 'curd_app/main.html',context)

def detail(request,id):
    detail_data = get_object_or_404(Store,pk=id)
    comments = Comment.objects.filter(store_id = id)
    context = {
        "tradename": detail_data.tradename,
        "owner": detail_data.owner,
        "location": detail_data.location,
        "jobdetail": detail_data.jobdetail,
        "wage": detail_data.wage,
        "currentapplicant": detail_data.currentapplicant,
        "id": detail_data.id,
        "isapply": detail_data.isapply,
        "comments": comments,
        "image": detail_data.image,
    }
    return render(request, 'curd_app/detail.html',context)

def create_page(request):
    return render(request, 'curd_app/create.html')

def create(request):
    new_data = Store()
    new_data.tradename = request.POST['tradename']
    new_data.owner = request.POST['owner']
    new_data.location = request.POST['location']
    new_data.jobdetail = request.POST['jobdetail']
    new_data.wage = request.POST['wage']
    new_data.currentapplicant = request.POST['currentapplicant']
    new_data.image = request.FILES['image']
    new_data.save()
    return redirect('main')

def update_page(request,id):
    update_data = get_object_or_404(Store, pk = id)
    context = {
        'id': id,
        "tradename": update_data.tradename,
        "owner": update_data.owner,
        "location": update_data.location,
        "jobdetail": update_data.jobdetail,
        "wage": update_data.wage,
        "currentapplicant": update_data.currentapplicant,
        'image': update_data.image,
    }
    return render(request,'curd_app/update.html',context)

def update(request,id):
    update_data = get_object_or_404(Store, pk=id)
    update_data.tradename = request.POST['tradename']
    update_data.owner = request.POST['owner']
    update_data.location = request.POST['location']
    update_data.jobdetail = request.POST['jobdetail']
    update_data.wage = request.POST['wage']
    update_data.currentapplicant = request.POST['currentapplicant']
    update_data.image = request.FILES['image']
    update_data.save()
    return redirect('main')

def delete(request,id):
    delete_data = get_object_or_404(Store,pk=id)
    delete_data.delete()
    return redirect("main")

def apply(request,id):
    apply_data = get_object_or_404(Store, pk = id)
    apply_data.currentapplicant += 1
    apply_data.isapply = True
    apply_data.save()
    return redirect("detail",id)

def deapply(request,id):
    apply_data = get_object_or_404(Store, pk = id)
    apply_data.currentapplicant -= 1
    apply_data.isapply = False
    apply_data.save()
    return redirect("detail",id)

def create_comment(request,id):
    new_comment = Comment()
    new_comment.store_id = Store.objects.get(pk=id)
    new_comment.user = request.POST['user']
    new_comment.content = request.POST['content']
    new_comment.date = timezone.now()
    new_comment.save()
    return redirect("detail",id)

def delete_comment(request,id,comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    comment.delete()
    return redirect('detail',id)

def master(request):
    return render(request, 'curd_app/master.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request= request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password = password)
            if user is not None:
                login(request,user)
            return redirect("master")
    else:
        form = AuthenticationForm()
        return render(request, 'curd_app/login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect("master")

def signup_view(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect("master")
    else:
        form = UserCreationForm()
        return render(request, 'curd_app/signup.html', {'form': form})

