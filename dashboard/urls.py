from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('boutique_list/', views.boutique_list, name='boutique_list'),
    path('boutique/<int:user_id>/', views.boutique, name='boutique'),
]
