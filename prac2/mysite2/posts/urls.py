from django.urls import path
from .views import posts_list, posts_detail

app_name = 'posts'

urlpatterns = [
    path("", posts_list),
    path("<slug:slug>/", posts_detail)
]