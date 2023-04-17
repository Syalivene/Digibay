from django.urls import path


from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete_conversation', views.delete_conversation, name='delete_conversation'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]