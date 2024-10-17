from django.contrib import admin
from django.urls import path
from blog.views import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', PostView.as_view(), name='home'),
]
