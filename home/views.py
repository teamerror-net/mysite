from django.shortcuts import render,redirect
from django.views import View
from account.models import Users
# Create your views here.
class UserDashboard(View):
    def get(self, request):
        user = Users.objects.get(id = request.user.id)
        data ={
            "user": user,
        }
        return render(request, 'dashboard.html',data)
    

class AdminDashboard(View):
    def get(self, request):
        user = Users.objects.get(id = request.user.id)
        data ={
            "user": user,
        }
        return render(request, 'admin_dashboard.html',data)
    
    def post(self, request):
        req_date = request.POST.get('date')
        search_user = []
        user = Users.objects.all()
        for x in user:
            if x.account_open == req_date:
                search_user.append(x)
        data ={
            "user": search_user,
        }
        for y in search_user:
            print(y.username)
        return render(request, 'user_details.html',data)
    
class DeleteUser(View):
    def get(self,request):
        return render(request, 'deleteuser.html')
    def post(self,request):
        req_user = request.POST.get('username')
        user = Users.objects.get(username=req_user)
        user.delete()
        return render(request, 'deleteuser.html')

class UpdateUser(View):
    def get(self,request):
        return render(request, 'update_user.html')
    def post(self,request):
        pass