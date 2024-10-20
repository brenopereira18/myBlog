from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
