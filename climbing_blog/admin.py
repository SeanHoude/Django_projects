from django.contrib import admin
from climbing_blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
