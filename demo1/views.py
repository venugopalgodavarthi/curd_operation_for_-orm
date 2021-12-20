from django.shortcuts import redirect, render
from django.http import HttpResponse
from demo1.models import student
# Create your views here.
def insert(request):
    if request.method=="POST":
        sname =request.POST['sname']
        marks= request.POST['marks']
        doj= request.POST['doj']
        print(sname,marks,doj)
        student.objects.create(sname=sname,marks=marks,doj=doj)
        #return HttpResponse('insert')
        return redirect('select')
    return render(request,'insert.html')


def select(request):
    res=student.objects.all()
    return render(request,'select.html',{'res':res})


def update(request):
    if request.method=='POST':
        sid= request.POST['sid']
        res=student.objects.filter(sid=sid)
        return render(request,'update.html',{'res':res})
    return render(request,'update.html')

def update_value(request,sid):
    if request.method=="POST":
        sname =request.POST['sname']
        marks= request.POST['marks']
        doj= request.POST['doj']
        print(sname,marks,doj)
        res=student.objects.filter(sid=sid).update(sname=sname,marks=marks,doj=doj)
        #return HttpResponse('update')
        return redirect('select')
    return render(request,'insert.html')


def delete(request):
    if request.method=='POST':
        sid= request.POST['sid']
        res=student.objects.filter(sid=sid)
        return render(request,'delete.html',{'res':res})
    return render(request,'delete.html')

def delete_value(request,sid):
    if request.method=="POST":
        res=student.objects.filter(sid=sid).delete()
        #return HttpResponse('update')
        return redirect('select')
    