from django.urls import path
from home.views import UserDashboard,AdminDashboard,DeleteUser,UpdateUser
urlpatterns = [
    path('dashboard',UserDashboard.as_view(), name = 'dashboard'),
    path('admin_dashboard',AdminDashboard.as_view(), name = 'admin_dashboard'),
    path('delete_user',DeleteUser.as_view(), name = 'delete_user'),
    path('update_user',UpdateUser.as_view(), name = 'update_user'),
]