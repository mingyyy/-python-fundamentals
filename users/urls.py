from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='index.html'), name="logout"),
    # Registration Page
    path('register/', views.register, name='register'),
]