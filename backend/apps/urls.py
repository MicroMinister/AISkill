from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_root),
    path('api/articles/', views.ArticleListCreateView.as_view(), name='article-list-create'),
    path('api/articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('api/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('api/articles/<int:article_id>/post_comment/', views.post_comment, name='post-comment'),
]
