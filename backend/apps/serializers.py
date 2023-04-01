from rest_framework import serializers
from .models import CustomUser, Article, Category, Comment

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'pub_date', 'author', 'category']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    article = ArticleSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'pub_date', 'author', 'article']
