from django.shortcuts import render, get_object_or_404
from api.models import Article, ArticleCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def detail(request, pk, slug):
    article = get_object_or_404(Article, pk=pk, slug=slug)
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    context = {
        'article': article,
        'latest_article': latest_article,
    }
    return render(request, 'article/detail.html', context)


def category(request, name):
    art_category = get_object_or_404(ArticleCategory, name__iexact=name)
    articles = Article.objects.filter(category=art_category).order_by('-created_date')
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    page = request.GET.get('page')

    paginator = Paginator(articles, per_page=4)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator(paginator.num_pages)

    context = {
        'articles': articles,
        'latest_article': latest_article,
        'art_category': art_category,
    }
    return render(request, 'article/category.html', context)
