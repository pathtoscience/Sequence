from django import contrib
from django import urls
from django.urls import path
from django.conf.urls import include, url
from .views import *
from blog.views import *

urlpatterns = [
    url(r"", include("django.contrib.auth.urls")),
    
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', loginPage, name="logout"),

    path("", home, name="home"),
    path("project_index/", project_index, name="project_index"),
    path("<int:pk>/", project_detail, name="project_detail"),

    path("detail/<int:pk>/", service_detail, name="service_detail"),


    path("contact/", contact, name="contact"),
    path("blog/", blog_index, name="blog"),
    path("aboutus/", about, name="aboutus"),
]
