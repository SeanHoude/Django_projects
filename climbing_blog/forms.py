from django.forms import ModelForm
from climbing_blog.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
