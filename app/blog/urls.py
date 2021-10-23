from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('mix/', views.BlogViewMix.as_view(), name='blog-mix'),
]