from django.urls import path
from . import views

urlpatterns= [
    path("", views.homepage, name='homepage'),
    path("login/", views.user_login, name='user_login'),
    path("logout/", views.user_logout, name='user_logout'),
    path("registration/", views.sign_up, name='sign_up'),
]