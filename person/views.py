from itertools import chain
from operator import attrgetter
from datetime import date
from django.shortcuts import render, get_object_or_404
from api.models import Person, Film, Serial


def detail(request, first_name, last_name):
    person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
    today = date.today()
    age = None

    if person.birthdate is not None:
        age = today.year - person.birthdate.year - ((today.month, today.day) <
                                                    (person.birthdate.month, person.birthdate.day))

    person_type = []
    creator_list = []
    actor_list = []
    writer_list = []
    director_list = []

    if Serial.objects.filter(creator=person):
        person_type.append('Creator')
        creator_list = Serial.objects.filter(creator=person).order_by('-year')

    if Film.objects.filter(actors=person) or Serial.objects.filter(actors=person):
        person_type.append('Actor')
        films = Film.objects.filter(actors=person)
        serials = Serial.objects.filter(actors=person)

        actor_list = sorted(
            chain(films, serials),
            key=attrgetter('year'), reverse=True)
        actor_list_count = len(actor_list)

    if Film.objects.filter(writers=person):
        person_type.append('Writer')
        writer_list = Film.objects.filter(writers=person).order_by('-year')

    if Film.objects.filter(director=person):
        person_type.append('Director')
        director_list = Film.objects.filter(director=person).order_by('-year')

    context = {
        'person': person,
        'age': age,
        'person_type': person_type,
        'creator_list': creator_list,
        'writer_list': writer_list,
        'director_list': director_list,
        'actor_list': actor_list,
        'actor_list_count': actor_list_count,
    }
    return render(request, 'person/detail.html', context)
