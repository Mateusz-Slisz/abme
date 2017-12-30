from django.shortcuts import render, get_object_or_404
from api.models import Article


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)
