from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Hiretuber
# Create your views here.

def hiretuber(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["user_email"]
        user_id = request.POST["user_id"]
        tuber_id = request.POST["tuber_id"]
        tuber_name = request.POST["tuber_name"]
        city = request.POST["city"]
        state = request.POST["state"]
        mobile = request.POST["mobile"]
        message = request.POST["description"]

        hiretuber = Hiretuber(first_name=first_name, last_name =last_name, email =email, user_id =user_id, tuber_id =tuber_id, tuber_name =tuber_name, city =city, state =state, mobile =mobile, message =message)
        hiretuber.save()
        messages.success(request,"Thank you for hiring")
        return redirect('youtubers')