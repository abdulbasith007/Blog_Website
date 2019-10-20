from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PostsHomeView.as_view(),name='blog-home'),
    path('post/<int:pk>/update',views.PostsUpdateView.as_view(),name='update'),
    path('post/new/',views.PostsCreateView.as_view(),name='create'),
    path('post/<int:pk>/',views.PostsDetailView.as_view(),name='post-details'),
    path('post/<int:pk>/delete/',views.PostsDeleteView.as_view() ,name='delete'),
    path('user/<str:username>',views.UserPostsListView.as_view(),name='user-posts'),
]
