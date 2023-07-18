from django.contrib import admin
from .models import Person, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
