from django.urls import path
from account.views import LoginView,SignupView,Signout
urlpatterns = [
    path('',LoginView.as_view(), name = 'login'),
    path('signup',SignupView.as_view(), name = 'signup'),
    path('signout',Signout.as_view(), name = "signout"),
]