from django.contrib import admin
from .models import CustomUser, Category, Article, Comment

# 注册 CustomUser 模型
admin.site.register(CustomUser)

# 注册 Category 模型
admin.site.register(Category)

# 注册 Article 模型
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'pub_date')  # 列表页显示的字段
    list_filter = ('category',)  # 列表页过滤器
    search_fields = ('title', 'content')  # 搜索字段
    date_hierarchy = 'pub_date'  # 日期层次结构
    ordering = ('-pub_date',)  # 排序方式

# 注册 Comment 模型
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'article', 'pub_date')  # 列表页显示的字段
    list_filter = ('article',)  # 列表页过滤器
    search_fields = ('content',)  # 搜索字段
    date_hierarchy = 'pub_date'  # 日期层次结构
    ordering = ('-pub_date',)  # 排序方式
