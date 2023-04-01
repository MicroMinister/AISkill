from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import CustomUser, Article, Category, Comment
from .serializers import CustomUserSerializer, ArticleSerializer, CategorySerializer, CommentSerializer
from rest_framework.permissions import AllowAny

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        author = self.request.user if self.request.user.is_authenticated else None
        serializer.save(author=author)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.data.get('content', '')
    comment = Comment(content=content, author=request.user, article=article)
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('article-list-create', request=request, format=format),
        'comments': reverse('comment-list-create', request=request, format=format),
    })

