from django.urls import path

from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name="base"),
    path('<slug:slug>', views.PostDetail.as_view(), name="post-detail"),
    path('category/<slug:slug>', views.PostListCategories.as_view(),
         name="category-posts"),
    path('blog/subscribe', views.subscribe, name="subscribe-form"),
    path('posts/video', views.VideoListView.as_view(), name="video")
]
