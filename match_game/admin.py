from django.contrib import admin
from models import Pokemon, Team
# Register your models here.






class PokemonAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Name', {
            'fields': ('name', 'pokedex_id', 'team', 'image')
        }),
    )
    list_display = ('name', 'pokedex_id', 'team', 'image')
    list_filter = ('team',)
    ordering = ('name', 'pokedex_id', 'team')





class TeamAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Pokemon, PokemonAdmin)
