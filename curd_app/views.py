from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog,Store
from django.utils import timezone

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
    context = {
        "tradename": detail_data.tradename,
        "owner": detail_data.owner,
        "location": detail_data.location,
        "jobdetail": detail_data.jobdetail,
        "wage": detail_data.wage,
        "currentapplicant": detail_data.currentapplicant,
        "id": detail_data.id,
        "isapply": detail_data.isapply,
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
    return redirect("main")

def deapply(request,id):
    apply_data = get_object_or_404(Store, pk = id)
    apply_data.currentapplicant -= 1
    apply_data.isapply = False
    apply_data.save()
    return redirect("main")