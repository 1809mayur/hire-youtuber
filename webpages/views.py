from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber

# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    # youtubers = Youtuber.objects.all().filter(is_featured = True)     # this will directly handle queryset and display only those values which satisfied filter condition.
    featured_tubers = Youtuber.featured_tubers.all()     # new manager created at models which contain only those values in queryset that satisfied the condition given into model method.
    all_tubers = Youtuber.objects.all().order_by("-created_date")[:6]
    
    data = {
        'sliders':sliders,
        'teams':teams,
        'featured_tubers':featured_tubers,
        'all_tubers' : all_tubers,
        
    }
    return render(request,'webpages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'webpages/about.html',data)

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')
