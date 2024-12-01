from django.shortcuts import redirect ,render
from .models import Member

# Create your views here.

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(requset):
    return render(requset,'add.html')

def addrec(request):
    w=request.POST['name']
    x=request.POST['age']
    y=request.POST['address']
    z=request.POST['phoneno']
    mem=Member(name=w,age=x,address=y,phoneno=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(requset,id):
    mem=Member.objects.get(id=id)
    return render(requset,'update.html',{'mem':mem})

def uprec(request,id):
    w=request.POST['name']
    x=request.POST['age']
    y=request.POST['address']
    z=request.POST['phoneno']
    mem=Member.objects.get(id=id)
    mem.name=w
    mem.age=x
    mem.address=y
    mem.phoneno=z
    mem.save()
    return redirect("/")