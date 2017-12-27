from django.contrib import admin
from .models import Person, Category, Film, Serial, Filmcast, Serialcast

admin.site.register(Person)
admin.site.register(Film)
admin.site.register(Filmcast)
admin.site.register(Serial)
admin.site.register(Serialcast)

