from django.shortcuts import render,get_object_or_404
from .models import Posts
from django.contrib.auth.models import User
from django.views.generic import DeleteView,UpdateView,CreateView,ListView,DetailView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
#from django.http import HttpResponse
# Create your views here.
#def home(request):
#    context={'posts':Posts.objects.all()}
#    return render(request,'blogs/home.html',context)

class PostsHomeView(ListView):
    model=Posts
    context_object_name='posts'
    template_name='blogs/home.html'
    ordering=['-date_posted']
    paginate_by=4

class UserPostsListView(ListView):
    model=Posts
    paginate_by=4
    template_name='blogs/user_posts.html'
    context_object_name='posts'
    def get_queryset(self):
        usr=get_object_or_404(User,username=self.kwargs.get('username'))
        return Posts.objects.filter(author=usr).order_by('-date_posted')

class PostsDetailView(DetailView):
    model=Posts

class PostsDeleteView(LoginRequiredMixin ,UserPassesTestMixin ,DeleteView):
    model=Posts
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False


class PostsUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model=Posts
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False

class PostsCreateView(LoginRequiredMixin,CreateView):
    model=Posts
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

