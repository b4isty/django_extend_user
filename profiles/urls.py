from django.urls import path
from .views import CustomLogInView, Signup, IndexView
from django.contrib.auth.views import LogoutView

app_name = "profiles"

urlpatterns = [

    path('', IndexView.as_view(), name="profile_list"),
    path('login/', CustomLogInView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("signup/", Signup.as_view(), name="signup")

]
