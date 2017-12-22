from itertools import chain
from operator import attrgetter
from datetime import date
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404
from api.models import Person, Film, Serial
from search.views import Round
from django.db.models import Avg



def detail(request, first_name, last_name):
    person = get_object_or_404(Person, first_name=first_name, last_name=last_name)
    serials = Serial.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('serialrating__rate')), 0))
    films = Film.objects.get_queryset().annotate(
        average_score=Coalesce(Round(Avg('filmrating__rate')), 0))

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
    actor_list_count = None

    if films.filter(actors=person) or serials.filter(actors=person):
        person_type.append('Actor')
        f_actor = films.filter(actors=person)
        s_actor = serials.filter(actors=person)

        actor_list = sorted(
            chain(f_actor, s_actor),
            key=attrgetter('year'), reverse=True)
        actor_list_count = len(actor_list)

    if serials.filter(creators=person):
        person_type.append('Creator')
        creator_list = serials.filter(creators=person).order_by('-year')

    if films.filter(writers=person):
        person_type.append('Writer')
        writer_list = films.filter(writers=person).order_by('-year')

    if films.filter(directors=person):
        person_type.append('Director')
        director_list = films.filter(directors=person).order_by('-year')


    context = {
        'person': person,
        'films': films,
        'serials': serials,
        'age': age,
        'person_type': person_type,
        'creator_list': creator_list,
        'writer_list': writer_list,
        'director_list': director_list,
        'actor_list': actor_list,
        'actor_list_count': actor_list_count,
    }
    return render(request, 'person/detail.html', context)
