from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Youtuber
from django.contrib import messages

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by("-created_date")
    city_search = Youtuber.objects.values_list('city',flat = True).distinct('city')
    camera_type_search = Youtuber.objects.values_list('camera_type',flat = True).distinct('camera_type')
    category_search = Youtuber.objects.values_list('category',flat = True).distinct('category')

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact = city)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact = category)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact = camera_type)

    data = {
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
    }
    return render(request,'youtubers/youtubers.html',data)



def youtubers_detail(request,id):
    # tuber_detail = get_object_or_404(Youtuber,id) or get_object(Youtuber,pk = id)
    tuber = Youtuber.objects.order_by("-created_date").get(pk=id)
    data = {
        'tuber' : tuber,
    }
    return render(request,"youtubers/youtuber_detail.html",data)




def search(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city',flat = True).distinct('city')
    camera_type_search = Youtuber.objects.values_list('camera_type',flat = True).distinct('camera_type')
    category_search = Youtuber.objects.values_list('category',flat = True).distinct('category')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            tubers = Youtuber.objects.order_by('-created_date').filter(description__icontains=keywords)
            tubers = tubers.union(Youtuber.objects.all().filter(first_name__icontains=keywords))

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact = city)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact = category)

    if 'camera' in request.GET:
        camera_type = request.GET['camera']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact = camera_type)
    
    # if no tubers present in our database then it throw an error of no such tuber exist search for something else.
    if tubers.count() == 0:
        messages.warning(request,"No such tuber present")
        return redirect('search')

  
  
    data = {
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' :category_search,
    }
    return render(request,'youtubers/search.html',data)