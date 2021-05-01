from django.shortcuts import render,redirect
from .models import ReachUs
from django.contrib import messages

# Create your views here.
def reachus(request):
    if request.method == "POST":
        full_name = request.POST["fullname"]
        mobile_number = request.POST["mobile_number"]
        email = request.POST.get("email",False)
        company_name = request.POST["company_name"]
        subject = request.POST["subject"]
        details = request.POST["details"]

    # add some filter over mobile_number or other fields whichever you want.
    reachus = ReachUs(full_name = full_name, mobile =mobile_number, email =email, company_name=company_name,subject =subject,details =details)
    reachus.save()
    messages.success(request,"Thankyou for contacting us.")
    return redirect("contact")