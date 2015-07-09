from django.contrib import admin

# Register your models here.

from .models import Person, Blog, Pizza, Topping

admin.site.register(Person)
admin.site.register(Blog)
admin.site.register(Pizza)
admin.site.register(Topping)
