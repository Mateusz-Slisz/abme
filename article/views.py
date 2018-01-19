from django.shortcuts import render, get_object_or_404
from api.models import Article, ArticleCategory


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    context = {
        'article': article,
        'latest_article': latest_article,
    }
    return render(request, 'article/detail.html', context)


def category(request, name):
    art_category = get_object_or_404(ArticleCategory, name__iexact=name)
    articles = Article.objects.filter(category=art_category)
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    context = {
        'articles': articles,
        'latest_article': latest_article,
        'art_category': art_category,
    }
    return render(request, 'article/category.html', context)
