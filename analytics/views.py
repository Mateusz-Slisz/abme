from django.shortcuts import render, get_object_or_404


def main(request):

    context = {

    }
    return render(request, 'analytics/main.html', context)
