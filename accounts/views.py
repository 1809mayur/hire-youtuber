from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from hireyoutuber.models import Hiretuber
# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        user_email = request.POST['user_email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    
        if password == confirm_password:
            if User.objects.filter(username =user_name).exists():
                messages.warning(request,"User exist, try another username")
                return redirect('register')
            else:
                if User.objects.filter(email =user_email).exists():
                    messages.warning(request,"Email already exist")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name =first_name, last_name =last_name, username =user_name, email =user_email, password =password)
                    user.save()
                    messages.success(request,"User Created Successfully")
                    return redirect('login')                    
        else:
            messages.warning(request,"Password do not matched")
            return redirect('register')

    return render(request,'accounts/register.html')



def login(request):
    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username =username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged in"+","+ username)
            return redirect('dashboard') 
        else:
            messages.warning(request,"Inavalid Credentials")
            return redirect('register')

    return render(request,'accounts/login.html')



def logout_user(request):

    logout(request)
    messages.success(request,"Logout")
    return redirect('home')


@login_required(login_url = "login")
def dashboard(request):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    
    user_hire = Hiretuber.objects.filter(user_id =user_id)
    unique_tuber = user_hire.distinct("tuber_name")
    data = {
        "user_hire": user_hire,
        "unique_tuber": unique_tuber,
    }

    return render(request,'accounts/dashboard.html',data)
