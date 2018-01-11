from django.shortcuts import render, get_object_or_404
from api.models import Article


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    latest_article = Article.objects.get_queryset().order_by('-created_date').first()

    context = {
        'article': article,
        'latest_article': latest_article,
    }
    return render(request, 'article/detail.html', context)
