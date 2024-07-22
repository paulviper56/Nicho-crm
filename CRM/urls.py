from django.urls import path
from . import views

urlpatterns= [
    path("", views.homepage, name='homepage'),
    path("user_login/", views.user_login, name='user_login'),
    path("logout/", views.user_logout, name='user_logout'),
    path("customer_registration/", views.customer_registration, name='customer_registration'),
    path("registration",views.registration, name='registration')
]