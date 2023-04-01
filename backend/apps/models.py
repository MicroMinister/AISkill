from django.contrib.auth.models import AbstractUser
from django.db import models

# 自定义用户模型
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # 自我介绍
    # 添加其他自定义字段
    

    def __str__(self):
        return self.username

# 类别模型
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 类别名称
    description = models.TextField(blank=True, null=True)  # 类别描述

    def __str__(self):
        return self.name

# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=200)  # 文章标题
    content = models.TextField()  # 文章内容
    pub_date = models.DateTimeField(auto_now_add=True)  # 发布日期
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 作者，与自定义用户模型关联
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 文章类别，与类别模型关联

    def __str__(self):
        return self.title

# 评论模型
class Comment(models.Model):
    content = models.TextField()  # 评论内容
    pub_date = models.DateTimeField(auto_now_add=True)  # 发布日期
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 评论作者，与自定义用户模型关联
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 所评论的文章，与文章模型关联

    def __str__(self):
        return self.content[:50]
