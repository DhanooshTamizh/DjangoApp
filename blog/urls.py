from django.urls import path
from . import views
from .views import PostListView, PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-post'),
    path('posts/<int:pk>', views.PostDetail, name='blog-post-detail'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name='blog-post-update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='blog-post-delete'),
    path('posts/new', PostCreateView.as_view(), name='blog-post-create'),
    path('about/',views.about,  name= 'blog-about'),
    path('likes/<int:pk>', views.LikeView, name='like_post'),

    ]