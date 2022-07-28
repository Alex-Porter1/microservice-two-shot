from django.contrib import admin

# Register your models here.
from .models import Hat, LocationVO

@admin.register(Hat)
class HatAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationVO)
class LocationVOAdmin(admin.ModelAdmin):
    pass
