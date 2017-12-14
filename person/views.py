from django.shortcuts import render, get_object_or_404
from api.models import Person, Film, Serial


def detail(request, first_name, last_name):
    person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
    

    context = {
        'person': person,
        
    }
    return render(request, 'person/detail.html', context)
