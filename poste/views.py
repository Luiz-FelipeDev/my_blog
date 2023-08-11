from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from poste.models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'homeblog.html', context)

class HomePostView(ListView):
    model = Post
    template_name = 'homeblog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        ''' O user é o  cara que tá logado e usa ele como autor o post '''
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        ''' O user é o  cara que tá logado e usa ele como autor o post '''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'confirm_post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False







def about(request):
    return render(request, 'aboutblog.html')

