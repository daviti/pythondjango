from django.contrib import admin

from.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    List_display = ['name', 'species', 'breed', 'age', 'sex']
