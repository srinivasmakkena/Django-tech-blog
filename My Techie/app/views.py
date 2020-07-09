from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Posts
import mammoth
import os
import random
from django.conf import settings
def home(request):
    if request.method=='POST':
        text=request.POST.get('text')
        file=request.FILES['filename']
        img=request.FILES['img']
        u=Posts(file=file,img=img,txt=text)
        u.save()
    p=list(Posts.objects.all())
    if(len(p)>4):
        p=p[:4]
    return render(request,'index.html',{'year':datetime.now(),'posts':p,'bgb':bgb()})
def all(request):
    p=list(Posts.objects.all())
    return render(request,'all.html',{'year':datetime.now(),'posts':p,'bgb':bgb()})
def delete(request):
    if request.method=='POST':
        id=request.POST.get('Delete')
        try:
            os.remove('.'+Posts.objects.all().filter(id=id)[0].img.url)
            os.remove('.'+Posts.objects.all().filter(id=id)[0].file.url)
            Posts.objects.all().filter(id=id).delete()
        except:
            Posts.objects.all().filter(id=id).delete()
    p=list(Posts.objects.all())
    return render(request,'delete.html',{'year':datetime.now(),'posts':p})
def about(request):
    return render(request,'about.html',{'year':datetime.now()})
def blog(request):
    id=(request.GET.get('id'))
    p=list(Posts.objects.filter(id=id))[0]
    print(p)
    s=settings.MEDIA_ROOT+str(p.file)
    with open(s, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
    p.file=result.value
    return render(request,'blog.html',{'year':datetime.now(),'posts':p,'bgb':bgb()})
def upload(request):
    return render(request,'upload.html',{'year':datetime.now(),'bgb':bgb()})
def bgb():
    bg=[]
    bgpath=settings.STATIC_ROOT+str('/bg')
    for r,d,f in os.walk(bgpath):
        for i in f:
            bg.append(i)
    return random.choice(bg)
