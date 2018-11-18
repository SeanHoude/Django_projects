from django.shortcuts import render, redirect
from climbing_blog.forms import ArticleForm
from climbing_blog.models import Article
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles
    })

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {
        'article': article
    })

@login_required
def edit_article(request, slug):
    article = Article.objects.get(slug=slug)
    # Check that the logged in user is the owner, if not, raise Http404 error
    if article.user != request.user:
        raise Http404
    # set the form we are using.
    form_class = ArticleForm
    # if coming to view from a submitted form...
    if request.method == 'POST':
        # grab the data from the submitted form.
        form = form_class(data=request.POST, instance=article)
        if form.is_valid():
            # and save it.
            form.save
            return redirect('article_detail', slug=article.slug)
    # otherwise, create a new form.
    else:
        form = form_class(instance=article)
    # render the template
    return render(request, 'articles/edit_article.html', {
        'article': article,
        'form': form,
    })

def create_article(request):
    form_class = ArticleForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.slug = slugify(article.title)
            article.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = form_class()

    return render(request, 'articles/create_article.html', {
        'form': form,
    })

def browse_by_title(request, initial=None):
    if initial:
        articles = Article.objects.filter(title__istartswith=initial).order_by('title')
    else:
        articles = Article.objects.all().order_by('title')
    
    return render(request, 'search/search.html', {
        'articles': articles,
        'initial': initial,
    })
