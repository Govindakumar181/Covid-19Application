from django.shortcuts import render,HttpResponse
from pakistan.models import *
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    World = world.objects.all()
    Pakistan = pakistan.objects.all()
    Pakistan_hospitals = pakistan_hospitals.objects.all()

    paginator=Paginator(Pakistan_hospitals,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        Pakistan_hospitals=paginator.page(page)
    except(EmptyPage,InvalidPage):
        Pakistan_hospitals=paginator=paginator.page(paginator.num_pages)

    content = {'World':World,'Pakistan':Pakistan,'Pakistan_hospitals':Pakistan_hospitals}
    return render(request,'index.html',content)

def search(request):
    query=request.GET['myCountry']
    if len(query)>100:
        # allPosts=[]
        Pakistan_hospitals=pakistan_hospitals.objects.none()
    else:
        Pakistan_hospitals_name=pakistan_hospitals.objects.filter(hospital_name__icontains=query)
        Pakistan_hospitals_address=pakistan_hospitals.objects.filter(hospital_address__icontains=query)
        Pakistan_hospitals=Pakistan_hospitals_name.union(Pakistan_hospitals_address)
    if Pakistan_hospitals.count() < 1:
        messages.error(request,"No search results found please search with another query")
    if len(query)<1:
        # allPosts=[]
        Pakistan_hospitals=pakistan_hospitals.objects.none()
    # allPosts:Post.objects.all()

    params={'Pakistan_hospitals':Pakistan_hospitals,'query':query}
    return render(request,'search.html',params)

    # return HttpResponse('search')
def karachi(request):
    World = world.objects.all()
    Pakistan = pakistan.objects.all()
    Pakistan_hospitals = pakistan_hospitals.objects.all()

    paginator=Paginator(Pakistan_hospitals,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        Pakistan_hospitals=paginator.page(page)
    except(EmptyPage,InvalidPage):
        Pakistan_hospitals=paginator=paginator.page(paginator.num_pages)

    content = {'World':World,'Pakistan':Pakistan,'Pakistan_hospitals':Pakistan_hospitals}
    return render(request,'karachi.html',content)
def islamabad(request):
    World = world.objects.all()
    Pakistan = pakistan.objects.all()
    Pakistan_hospitals = pakistan_hospitals.objects.all()

    paginator=Paginator(Pakistan_hospitals,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1

    try:
        Pakistan_hospitals=paginator.page(page)
    except(EmptyPage,InvalidPage):
        Pakistan_hospitals=paginator=paginator.page(paginator.num_pages)

    content = {'World':World,'Pakistan':Pakistan,'Pakistan_hospitals':Pakistan_hospitals}
    return render(request,'islamabad.html',content)