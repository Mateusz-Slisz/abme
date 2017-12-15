from itertools import chain
from operator import attrgetter
from django.shortcuts import render, get_object_or_404
from api.models import Person, Film, Serial


def detail(request, first_name, last_name):
    person = get_object_or_404(Person, first_name=first_name, last_name=last_name)

    person_type = []
    creator_list = []
    actor_list = []
    writer_list = []
    director_list = []

    if Serial.objects.filter(creator=person):
        person_type.append('Creator')
        creator_list = Serial.objects.filter(creator=person).order_by('year')

    if Film.objects.filter(actors=person) or Serial.objects.filter(actors=person):
        person_type.append('Actor')
        films = Film.objects.filter(actors=person)
        serials = Serial.objects.filter(actors=person)

        actor_list = sorted(
            chain(films, serials),
            key=attrgetter('year'))

    if Film.objects.filter(writers=person):
        person_type.append('Writer')
        writer_list = Film.objects.filter(writers=person).order_by('year')

    if Film.objects.filter(director=person):
        person_type.append('Director')
        director_list = Film.objects.filter(director=person).order_by('year')

    context = {
        'person': person,
        'person_type': person_type,
        'creator_list': creator_list,
        'writer_list': writer_list,
        'director_list': director_list,
        'actor_list': actor_list,
    }
    return render(request, 'person/detail.html', context)
