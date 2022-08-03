from django.urls import path

from .views import Signin, logoutUser, Signup
urlpatterns = [
    path('login/', Signin.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
]