    
from django.http import HttpResponse
from django.shortcuts import render
# from . import open
from mysiteapp.models import Upload_Item

def index1(request):
    return render(request,"index1.html")
def about(request):
    return HttpResponse('''<h1>this is goggle about page <a href="https://about.google/">google about</a></h1>''')
def open(request):
    try:
        with open("open.txt","r") as file:
            data=file.read()
    except Exception:
        data="</h2> this file does not exist</h2>"
    return HttpResponse(data)


def removepunc(request):
    return HttpResponse("hello")
def capitalizefirst(request):
    return HttpResponse("capital")
def spaceremove(request):
    return HttpResponse("spaceremove")
def newlineremove(request):
    return HttpResponse("newlineremove")



def prodview(request):
    servicedata=Upload_Item.objects.filter(id=2)
    return render(request,"prodview.html",{"servicedata":servicedata})



def index(request):
    servicedata = Upload_Item.objects.all()
    if request.method=="GET":
        st=request.GET.get("val")
        if st!=None:
            servicedata=Upload_Item.objects.filter(item_name__contains=st)
    data={"servicedata":servicedata}
    
    return render(request,"index.html",data)
