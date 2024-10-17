from django.urls import path
from .views import PostListView, PostDetailView


urlpatterns = [
    path('home/', PostListView.as_view(), name='home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
]