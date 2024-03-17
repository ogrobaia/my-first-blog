from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_urls, name='post_list')
]