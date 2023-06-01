from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('users', views.user_list, name='user_list'),
    path('users/<int:id>', views.user_detail, name='user_detail'),
    path('new_user', views.user_create, name='user_create'),
]
