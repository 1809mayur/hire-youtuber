from django.shortcuts import render

from .models import Links

# Create your views here.
def links(request):
    addresses = Links.objects.get(pk=1)
    data = {
        'addresses':addresses,
    }

    return render(request,"includes/footer.html",data)