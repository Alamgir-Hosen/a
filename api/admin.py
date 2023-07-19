from django.contrib import admin
from api.models import Breed

class BreedAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'size']
admin.site.register(Breed, BreedAdmin)
