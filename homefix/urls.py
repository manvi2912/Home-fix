from django.contrib import admin
from django.urls import path
from homefix import views

urlpatterns = [
    path("", views.index, name='home'),
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("area_service", views.area_service, name="area_service"),
    path("details", views.details, name="details"),
    path("contactus", views.contactus, name="contactus"),
    path("myservices", views.myservices, name="myservices"),
    path("cancel", views.cancel, name="cancel_req"),
    path("rating", views.rating, name="rating"),
    path("reviews", views.reviews, name="reviews"),
]