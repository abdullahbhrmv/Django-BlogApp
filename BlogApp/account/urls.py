from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),       # /login/ için LoginView kullanacak
    path("register/", views.RegisterView.as_view(), name="register"),  # /register/ için RegisterView kullanacak
    path("logout/", views.LogoutView.as_view(), name="logout"),    # /logout/ için LogoutView kullanacak
]
