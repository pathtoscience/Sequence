from django.urls import path
from .views import *

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("<int:pk>/", blog_detail, name="blog_detail"),
    path("<category>/", blog_category, name="blog_category"),
]