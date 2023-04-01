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
        author = validated_data.pop('author')
        category = validated_data.pop('category')
        user = CustomUser.objects.get(id=author.id)
        category_obj = Category.objects.get(id=category.id)
        article = Article.objects.create(author=user, category=category_obj, **validated_data)
        return article

class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    article = ArticleSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'pub_date', 'author', 'article']
