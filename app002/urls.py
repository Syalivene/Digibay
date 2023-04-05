from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'app002'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.my_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app002/login.html', authentication_form=LoginForm), name='login'),
]
