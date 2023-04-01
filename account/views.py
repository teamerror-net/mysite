from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from account.models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from datetime import datetime
import pytz



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = username.lower()
        user = authenticate(username = username,password = password)
        if user is None:
            return HttpResponse('Invalid Login details')
        if user is not None:
            auth_login(request,user)
            chk_user = Users.objects.get(id = request.user.id)
            if chk_user.is_superuser == True and chk_user.is_staff == True:
                return redirect('admin_dashboard')
            if chk_user.is_superuser == False and chk_user.is_staff == False:
                if chk_user.is_signin == False:
                    present = chk_user.present
                    chk_user.present = int(present) + 1
                    chk_user.is_signin = True
                    chk_user.save()
                    return redirect('dashboard')
                elif chk_user.is_signin == True:
                    return redirect('dashboard')
    

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        username = username.lower()
        time_zone = pytz.timezone('Asia/Dubai')
        localtime= datetime.now(time_zone)
        t_date=int(localtime.strftime("%d"))
        t_month=int(localtime.strftime("%m"))
        t_year=int(localtime.strftime("%Y"))
        date= str(t_date) + '-' + str(t_month) + '-' + str(t_year)
        account_open = date
        current_time = localtime.strftime("%I:%M:%S")
        account_open_time = current_time
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if Users.objects.filter(username = username):
            messages.info(request, "username already exist.")
            return redirect('signup')

        if password != confirm_password:
            return HttpResponse('Password is not Match')
        
        else:
            create_new_user = Users.objects.create_user(username=username,password=password,gender=gender,account_open=account_open,account_open_time=account_open_time)
            create_new_user.set_password(password)
            create_new_user.save()
            messages.success(request, 'Successfully Signup!')
            return redirect('login')
        
class Signout(View):
    def get(self,request):
        logout(request)
        return redirect('login')